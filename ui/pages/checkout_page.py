from ui.pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Оформление заказа: данные покупателя + подтверждение."""

    FIRST_NAME = "[data-test='firstName']"
    LAST_NAME = "[data-test='lastName']"
    POSTAL_CODE = "[data-test='postalCode']"
    CONTINUE = "[data-test='continue']"
    FINISH = "[data-test='finish']"
    COMPLETE_HEADER = "[data-test='complete-header']"
    ERROR = "[data-test='error']"

    def fill_info(self, first: str, last: str, postal: str) -> "CheckoutPage":
        self.page.fill(self.FIRST_NAME, first)
        self.page.fill(self.LAST_NAME, last)
        self.page.fill(self.POSTAL_CODE, postal)
        self.page.click(self.CONTINUE)
        return self

    def finish(self) -> "CheckoutPage":
        self.page.click(self.FINISH)
        return self

    def complete_header(self) -> str:
        return self.page.text_content(self.COMPLETE_HEADER) or ""

    def error_message(self) -> str:
        return self.page.text_content(self.ERROR) or ""
