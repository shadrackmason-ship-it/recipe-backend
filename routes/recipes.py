from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix = "/recipes",
    tags = ["Recipes"]
)

class Recipe(BaseModel):
    title: str
    description: str
    category: str
    prep_time: int
    cook_time: int
    servings: int

recipes = []

@router.get("/")
def get_recipes():
    return {"recipes": recipes}

@router.get("/{recipe_id}")
def get_recipe(recipe_id: int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            return recipe
    return {
        "message": "Recipe not found"
    }

@router.post("/")
def create_recipe(recipe: Recipe):
    new_recipe = {
        "id": len(recipes) + 1,
        "title": recipe.title,
        "description": recipe.description,
        "category": recipe.category,
        "prep_time": recipe.prep_time,
        "cook_time": recipe.cook_time,
        "servings": recipe.servings
    }
    recipes.append(new_recipe)
    return {
        "message": "Recipe created",
        "recipe": new_recipe
    }