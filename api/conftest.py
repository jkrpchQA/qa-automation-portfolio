import pytest

from api.client import PlaceholderClient


@pytest.fixture(scope="session")
def client() -> PlaceholderClient:
    """Один клиент на всю сессию — переиспользуем TCP-соединение."""
    return PlaceholderClient()


@pytest.fixture
def post_payload() -> dict:
    return {"title": "QA automation", "body": "portfolio test", "userId": 1}
