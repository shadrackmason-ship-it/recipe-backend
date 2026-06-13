from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "backend running"
    }

def test_get_recipes():
    response = client.get("/recipes/")
    assert response.status_code == 200

def test_create_recipe():
    recipe = {
        "title": "Pancakes",
        "description": "Easy breakfast", 
        "category": "Breakfast",
        "prep_time": 10,
        "cook_time": 15,
        "servings": 4
    }
    response = client.post("/recipes/", json=recipe)
    assert response.status_code == 200
    data = response.json()
    assert data["recipe"]["title"] == "Pancakes"