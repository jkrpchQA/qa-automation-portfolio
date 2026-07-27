from ui.pages.base_page import BasePage
from ui.pages.checkout_page import CheckoutPage


class CartPage(BasePage):
    """Корзина."""

    CART_ITEM = ".cart_item"
    CHECKOUT_BUTTON = "[data-test='checkout']"

    def items_count(self) -> int:
        return self.page.locator(self.CART_ITEM).count()

    def checkout(self) -> CheckoutPage:
        self.page.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.page, self.base_url)
