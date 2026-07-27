import pytest

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_get_all_posts(client):
    resp = client.get_posts()
    assert resp.status_code == 200
    assert len(resp.json()) == 100


def test_get_single_post(client):
    resp = client.get_post(1)
    assert resp.status_code == 200
    body = resp.json()
    assert body["id"] == 1
    assert set(body.keys()) == {"userId", "id", "title", "body"}


def test_filter_posts_by_user(client):
    resp = client.get_posts(userId=1)
    assert resp.status_code == 200
    posts = resp.json()
    assert len(posts) > 0
    assert all(post["userId"] == 1 for post in posts)


def test_get_post_comments(client):
    resp = client.get_post_comments(1)
    assert resp.status_code == 200
    comments = resp.json()
    assert len(comments) > 0
    assert all(comment["postId"] == 1 for comment in comments)
