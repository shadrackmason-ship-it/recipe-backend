from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.recipe import Recipe as RecipeModel
from app.schemas.recipe import RecipeCreate, RecipeResponse

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
        servings=recipe.servings
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.get("/", response_model=list[RecipeResponse])
def get_recipes(db: Session = Depends(get_db), page: int = 1, limit: int = 10):
    skip = (page - 1) * limit
    total = db.query(RecipeModel).count()
    recipes = (db.query(RecipeModel).offset(skip).limit(limit).all())
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
    db.commit()
    db.refresh(recipe)
    return recipe

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = db.query(RecipeModel).filter(RecipeModel.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return {
        "message": "Recipe deleted"
    }
