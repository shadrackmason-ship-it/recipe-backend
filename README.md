# recipe-backend

A backend API for recipe community features built with FastAPI.

## Setup

- Create a virtual environment: `python3 -m venv venv`
- Activate it: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`

## Running Locally

- `uvicorn app.main:app --reload`

## Running with Docker

- `docker build -t recipe-backend .`
- `docker run -p 8000:8000 recipe-backend`

## Running Tests

- `venv/bin/pytest -v`

## Endpoints

- `POST /api/recipes/{recipe_id}/favorite` - Favorite a recipe
- `DELETE /api/recipes/{recipe_id}/favorite` - Unfavorite a recipe
- `POST /api/recipes/{recipe_id}/reviews` - Add a review
- `GET /api/recipes/{recipe_id}/reviews` - Get reviews for a recipe
