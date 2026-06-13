import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, Base, engine,SessionLocal

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app.dependency_overrides[get_db] = override_get_db

def test_home():
    response = client.get("/")
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
    assert response.json()["title"] == "Pancakes"

def test_update_recipe():
    recipe = {
        "title": "Pizza",
        "description": "Cheese pizza",
        "category": "Dinner",
        "prep_time": 20,
        "cook_time": 25,
        "servings": 4
    }
    create = client.post("/recipes/", json=recipe)
    recipe_id = create.json()["id"]
    updated = {
        "title": "Pepperoni Pizza",
        "description": "Cheese and pepperoni",
        "category": "Dinner",
        "prep_time": 20,
        "cook_time": 30,
        "servings": 4
    }
    response = client.put(f"/recipes/{recipe_id}", json=updated)
    assert response.status_code == 200
    assert response.json()["title"] == "Pepperoni Pizza"

def test_delete_recipe():
    recipe = {
        "title": "Burger",
        "description": "Beef burger",
        "category": "Lunch",
        "prep_time": 15,
        "cook_time": 15,
        "servings": 2
    }
    create = client.post("/recipes/", json=recipe)
    recipe_id = create.json()["id"]
    response = client.delete(f"/recipes/{recipe_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Recipe deleted"
