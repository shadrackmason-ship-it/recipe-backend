from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_search_recipes():
    response = client.get("/search/?q=chicken")
    assert response.status_code == 200