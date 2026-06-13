# recipe-backend

A FastAPI backend for managing recipe community features like favorites and reviews.

## Tech Stack

- FastAPI
- SQLAlchemy + SQLite
- Pydantic
- Docker
- pytest

## Project Structure

```
recipe-backend/
├── app/
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   ├── database.py     # DB connection and session
│   └── main.py         # App entry point
├── routes/
│   └── community.py    # Favorites and reviews routes
├── tests/
│   └── test_community.py
├── conftest.py
├── Dockerfile
└── requirements.txt
```

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/api/recipes/{recipe_id}/favorite` | Favorite a recipe | Yes |
| DELETE | `/api/recipes/{recipe_id}/favorite` | Unfavorite a recipe | Yes |
| POST | `/api/recipes/{recipe_id}/reviews` | Add a review | Yes |
| GET | `/api/recipes/{recipe_id}/reviews` | Get reviews for a recipe | No |

Protected routes require a Bearer token in the `Authorization` header.

## Running Locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Running with Docker

```bash
docker build -t recipe-backend .
docker run -p 8000:8000 recipe-backend
```

## Running Tests

```bash
source venv/bin/activate
venv/bin/pytest -v
```
