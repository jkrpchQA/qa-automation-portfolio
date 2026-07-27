from ui.pages.base_page import BasePage
from ui.pages.inventory_page import InventoryPage


class LoginPage(BasePage):
    """Страница логина. Локаторы через data-test — стабильны, не привязаны к вёрстке."""

    USERNAME = "[data-test='username']"
    PASSWORD = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR = "[data-test='error']"

    def open(self) -> "LoginPage":
        super().open("/")
        return self

    def login(self, username: str, password: str) -> InventoryPage:
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BUTTON)
        return InventoryPage(self.page, self.base_url)

    def error_message(self) -> str:
        return self.page.text_content(self.ERROR) or ""
