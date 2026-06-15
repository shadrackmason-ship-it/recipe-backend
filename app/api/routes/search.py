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

    return [r for r in fake_recipes if q.lower() in r["name"].lower()]


@router.get("/ingredients")
def search_by_ingredient(ingredient: str):
    return [
        r for r in fake_recipes
        if ingredient.lower() in [i.lower() for i in r["ingredients"]]
    ]


@router.get("/category")
def filter_by_category(category: str):
    return [r for r in fake_recipes if r["category"].lower() == category.lower()]