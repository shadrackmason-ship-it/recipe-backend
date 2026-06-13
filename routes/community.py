from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import community as community_models
from app.schemas import community as community_schemas
from app.database import get_db

# TEMP: Remove this after Feature 1 merges their JWT auth
from fastapi.security import HTTPBearer
security = HTTPBearer()

def get_current_user(token = Depends(security)):
    """Temporary fake auth. Replace with real one from Feature 1 later."""
    return {"id": 1, "username": "testuser"}

router = APIRouter(prefix="/api", tags=["Community"])

@router.post("/recipes/{recipe_id}/favorite", status_code=201)
def add_favorite(
    recipe_id: int, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    """
    Add a recipe to current user's favorites. Requires JWT auth.
    400 if already favorited. 404 if recipe doesn't exist.
    """
    # TODO: Uncomment when Feature 2 merges Recipe model
    # from app.models import recipe
    # recipe_obj = db.query(recipe.Recipe).filter(recipe.Recipe.id == recipe_id).first()
    # if not recipe_obj:
    #     raise HTTPException(status_code=404, detail="Recipe not found")
    
    existing = db.query(community_models.Favorite).filter(
        community_models.Favorite.user_id == current_user["id"],
        community_models.Favorite.recipe_id == recipe_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Already favorited")
    
    fav = community_models.Favorite(user_id=current_user["id"], recipe_id=recipe_id)
    db.add(fav)
    db.commit()
    return {"message": "Added to favorites"}

@router.delete("/recipes/{recipe_id}/favorite", status_code=204)
def remove_favorite(
    recipe_id: int, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    """Remove a recipe from current user's favorites."""
    fav = db.query(community_models.Favorite).filter(
        community_models.Favorite.user_id == current_user["id"],
        community_models.Favorite.recipe_id == recipe_id
    ).first()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(fav)
    db.commit()
    return

@router.post("/recipes/{recipe_id}/reviews", response_model=community_schemas.ReviewOut, status_code=201)
def create_review(
    recipe_id: int, 
    review: community_schemas.ReviewCreate, 
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    """Create a review for a recipe. Rating must be 1-5."""
    db_review = community_models.Review(
        **review.model_dump(), 
        user_id=current_user["id"], 
        recipe_id=recipe_id
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@router.get("/users/me/favorites", response_model=list[community_schemas.FavoriteOut])
def get_my_favorites(
    db: Session = Depends(get_db), 
    current_user = Depends(get_current_user)
):
    """Get all favorites for the current logged-in user."""
    return db.query(community_models.Favorite).filter(
        community_models.Favorite.user_id == current_user["id"]
    ).all()