import pytest

pytestmark = [pytest.mark.ui, pytest.mark.regression]


@pytest.mark.smoke
def test_full_checkout_flow(logged_in_page):
    logged_in_page.add_to_cart("sauce-labs-backpack")
    cart = logged_in_page.open_cart()
    assert cart.items_count() == 1

    checkout = cart.checkout()
    checkout.fill_info("Evgeniy", "QA", "10000").finish()
    assert "Thank you for your order" in checkout.complete_header()


@pytest.mark.negative
@pytest.mark.parametrize(
    "first, last, postal, expected_error",
    [
        ("", "QA", "10000", "First Name is required"),
        ("Evgeniy", "", "10000", "Last Name is required"),
        ("Evgeniy", "QA", "", "Postal Code is required"),
    ],
)
def test_checkout_requires_all_fields(logged_in_page, first, last, postal, expected_error):
    logged_in_page.add_to_cart("sauce-labs-backpack")
    cart = logged_in_page.open_cart()
    checkout = cart.checkout()
    checkout.fill_info(first, last, postal)
    assert expected_error in checkout.error_message()
