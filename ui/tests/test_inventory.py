import pytest

pytestmark = pytest.mark.ui


@pytest.mark.smoke
def test_inventory_shows_all_products(logged_in_page):
    assert logged_in_page.items_count() == 6


def test_add_items_updates_cart_badge(logged_in_page):
    logged_in_page.add_to_cart("sauce-labs-backpack")
    logged_in_page.add_to_cart("sauce-labs-bike-light")
    assert logged_in_page.cart_count() == 2
