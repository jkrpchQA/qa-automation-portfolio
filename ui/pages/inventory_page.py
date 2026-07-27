from ui.pages.base_page import BasePage
from ui.pages.cart_page import CartPage


class InventoryPage(BasePage):
    """Каталог товаров после успешного логина."""

    TITLE = ".title"
    INVENTORY_ITEM = ".inventory_item"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = "[data-test='shopping-cart-link']"

    def add_to_cart(self, item_id: str) -> "InventoryPage":
        # item_id, например: "sauce-labs-backpack"
        self.page.click(f"[data-test='add-to-cart-{item_id}']")
        return self

    def cart_count(self) -> int:
        badge = self.page.locator(self.CART_BADGE)
        return int(badge.text_content()) if badge.count() else 0

    def items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEM).count()

    def title(self) -> str:
        return self.page.text_content(self.TITLE) or ""

    def open_cart(self) -> CartPage:
        self.page.click(self.CART_LINK)
        return CartPage(self.page, self.base_url)
