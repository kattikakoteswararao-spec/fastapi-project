from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def test_create_user():
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"

    response = client.post(
        "/users/",
        json={
            "name": "Test User",
            "email": email,
            "age": 30
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert data["name"] == "Test User"
    assert data["email"] == email
    assert data["age"] == 30


def test_get_users_with_pagination():
    response = client.get("/users/?skip=0&limit=10")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_filter_users_by_name():
    response = client.get("/users/?name=Test")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_not_found():
    response = client.get("/users/999999")

    assert response.status_code == 404


def test_delete_user_not_found():
    response = client.delete("/users/999999")

    assert response.status_code == 404