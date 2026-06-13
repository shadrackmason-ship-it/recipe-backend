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

def test_update_recipe():
    recipe = {
        "title": "Pizza",
        "description": "Cheese pizza",
        "category": "Dinner",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4
    }
    create_response = client.post("/recipes/", json=recipe)
    recipe_id = create_response.json()["recipe"]["id"]
    updated_recipe = {
        "title": "Pepperoni Pizza",
        "description": "Cheese and pepperoni",
        "category": "Dinner",
        "prep_time": 20,
        "cook_time": 30,
        "servings": 4
    }
    response = client.put(f"/recipes/{recipe_id}", json=updated_recipe)
    assert response.status_code == 200

def test_delete_recipe():
    recipe = {
        "title": "Burger",
        "description": "Beef burger",
        "category": "Lunch",
        "prep_time": 15,
        "cook_time": 15,
        "servings": 2
    }
    create_response = client.post("/recipes/", json=recipe)
    recipe_id = create_response.json()["recipe"]["id"]
    response = client.delete(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Recipe deleted"