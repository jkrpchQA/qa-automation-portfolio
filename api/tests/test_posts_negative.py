import pytest

pytestmark = [pytest.mark.api, pytest.mark.negative]


def test_get_nonexistent_post_returns_404(client):
    assert client.get_post(9999).status_code == 404


def test_filter_by_nonexistent_user_returns_empty(client):
    resp = client.get_posts(userId=99999)
    assert resp.status_code == 200
    assert resp.json() == []
