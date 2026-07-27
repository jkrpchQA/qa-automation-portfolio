import pytest

pytestmark = pytest.mark.api


@pytest.mark.smoke
def test_create_post(client, post_payload):
    resp = client.create_post(post_payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == post_payload["title"]
    assert "id" in body


@pytest.mark.regression
def test_update_post_put(client, post_payload):
    updated = {**post_payload, "title": "Updated title"}
    resp = client.update_post(1, updated)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Updated title"


@pytest.mark.regression
def test_patch_post(client):
    resp = client.patch_post(1, {"title": "Patched title"})
    assert resp.status_code == 200
    assert resp.json()["title"] == "Patched title"


def test_delete_post(client):
    resp = client.delete_post(1)
    assert resp.status_code == 200
