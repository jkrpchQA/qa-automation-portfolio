import pytest

from ui.pages.login_page import LoginPage
from ui.pages.inventory_page import InventoryPage

BASE_URL = "https://www.saucedemo.com"

STANDARD_USER = "standard_user"
PASSWORD = "secret_sauce"


@pytest.fixture(autouse=True)
def _set_timeouts(page):
    """Запас по таймаутам, чтобы моргания сети/стенда не роняли тесты.

    Навигация (page.goto) — до 60 сек, ожидание элементов — до 15 сек.
    Работает вместе с автоповтором (--reruns) как две линии защиты от флаки.
    """
    page.set_default_navigation_timeout(60_000)
    page.set_default_timeout(15_000)


@pytest.fixture
def login_page(page) -> LoginPage:
    """Открытая страница логина. page — фикстура из pytest-playwright."""
    return LoginPage(page, BASE_URL).open()


@pytest.fixture
def logged_in_page(page) -> InventoryPage:
    """Пользователь уже залогинен и находится в каталоге."""
    login = LoginPage(page, BASE_URL).open()
    return login.login(STANDARD_USER, PASSWORD)
