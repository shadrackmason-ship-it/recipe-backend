from fastapi import APIRouter, Query

router = APIRouter(prefix="/search", tags=["Search"])

fake_recipes = [
    {"id": 1, "name": "Ugali Beef", "category": "local", "ingredients": ["ugali", "beef"]},
    {"id": 2, "name": "Pasta Carbonara", "category": "italian", "ingredients": ["pasta", "egg"]},
    {"id": 3, "name": "Chicken Curry", "category": "indian", "ingredients": ["chicken", "curry"]},
]

@router.get("/")
def search_recipes(q: str = Query(None)):
    if not q:
        return fake_recipes

    return [
        recipe for recipe in fake_recipes
        if q.lower() in recipe["name"].lower()
    ]

@router.get("/ingredients")
def search_by_ingredient(ingredient: str):
    return [
        recipe for recipe in fake_recipes
        if ingredient.lower() in [i.lower() for i in recipe["ingredients"]]
    ]

@router.get("/category")
def filter_by_category(category: str):
    return [
        recipe for recipe in fake_recipes
        if recipe["category"].lower() == category.lower()
    ]