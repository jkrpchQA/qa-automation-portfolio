import re

import pytest
from playwright.sync_api import expect

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_valid_login_opens_inventory(login_page):
    inventory = login_page.login("standard_user", "secret_sauce")
    expect(inventory.page).to_have_url(re.compile(r"/inventory\.html"))
    assert inventory.items_count() == 6


@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_password", "do not match"),
        ("ghost_user", "secret_sauce", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login_shows_error(login_page, username, password, expected_error):
    login_page.login(username, password)
    assert expected_error in login_page.error_message()


@pytest.mark.negative
def test_locked_out_user_cannot_login(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "locked out" in login_page.error_message()
