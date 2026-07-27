from playwright.sync_api import Page


class BasePage:
    """Базовый класс для всех страниц. Хранит page и base_url."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = "/") -> "BasePage":
        self.page.goto(f"{self.base_url}{path}")
        return self
