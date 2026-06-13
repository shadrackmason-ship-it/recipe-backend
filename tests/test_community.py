from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
HEADERS = {"Authorization": "Bearer testtoken"}

def test_favorite_recipe():
    response = client.post("/api/recipes/1/favorite", headers=HEADERS)
    assert response.status_code in [201, 409]

def test_create_review():
    payload = {"rating": 5, "comment": "Test review"}
    response = client.post("/api/recipes/1/reviews", json=payload, headers=HEADERS)
    assert response.status_code == 201
    assert response.json()["rating"] == 5

def test_get_reviews():
    response = client.get("/api/recipes/1/reviews")
    assert response.status_code == 200
    assert isinstance(response.json(), list)