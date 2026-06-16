import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.recipe import Recipe as RecipeModel
from app.schemas.recipe import RecipeCreate, RecipeResponse, RecipeListResponse

router = APIRouter(
    prefix="/recipes",
    tags=["Recipes"]
)

@router.post("/", response_model=RecipeResponse)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    new_recipe = RecipeModel(
        title=recipe.title,
        description=recipe.description,
        category=recipe.category,
        prep_time=recipe.prep_time,
        cook_time=recipe.cook_time,
        servings=recipe.servings,
        ingredients=json.dumps(recipe.ingredients),
        instructions=json.dumps(recipe.instructions)
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    new_recipe.ingredients = json.loads(new_recipe.ingredients)
    new_recipe.instructions = json.loads(new_recipe.instructions)
    return new_recipe

@router.get("/", response_model=RecipeListResponse)
def get_recipes(db: Session = Depends(get_db), page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    total = db.query(RecipeModel).count()
    recipes = db.query(RecipeModel).offset(skip).limit(limit).all()
    for r in recipes:
        r.ingredients = json.loads(r.ingredients) if r.ingredients else []
        r.instructions = json.loads(r.instructions) if r.instructions else []
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": recipes
    }

@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe.ingredients = json.loads(recipe.ingredients) if recipe.ingredients else []
    recipe.instructions = json.loads(recipe.instructions) if recipe.instructions else []
    return recipe

@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, updated_recipe: RecipeCreate, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    recipe.title = updated_recipe.title
    recipe.description = updated_recipe.description
    recipe.category = updated_recipe.category
    recipe.prep_time = updated_recipe.prep_time
    recipe.cook_time = updated_recipe.cook_time
    recipe.servings = updated_recipe.servings
    recipe.ingredients = json.dumps(updated_recipe.ingredients)
    recipe.instructions = json.dumps(updated_recipe.instructions)
    db.commit()
    db.refresh(recipe)
    recipe.ingredients = json.loads(recipe.ingredients)
    recipe.instructions = json.loads(recipe.instructions)
    return recipe

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted"}