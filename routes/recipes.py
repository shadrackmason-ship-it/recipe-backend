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

@router.post("/")
def create_recipe(recipe: Recipe):
    recipes.append(recipe.model_dump())
    return {
        "message": "Recipe created",
        "recipe": recipe
    }