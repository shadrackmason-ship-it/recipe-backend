from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.database import get_db
from app.models.community import Favorite, Review, Recipe
from app.schemas.community import ReviewCreate, ReviewOut, FavoriteOut, RecipeOut
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import List

router = APIRouter()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return token

@router.get("/api/recipes", response_model=List[RecipeOut])
def get_recipes(db: Session = Depends(get_db)):
    return db.query(Recipe).all()

@router.post("/api/recipes/{recipe_id}/favorite", status_code=201, response_model=FavoriteOut)
def add_favorite(recipe_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    existing = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.recipe_id == recipe_id).first()
    if existing:
        raise HTTPException(status_code=409, detail="Already favorited")
    
    fav = Favorite(user_id=user_id, recipe_id=recipe_id)
    db.add(fav)
    try:
        db.commit()
        db.refresh(fav)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Already favorited")
    return fav

@router.delete("/api/recipes/{recipe_id}/favorite", status_code=204)
def remove_favorite(recipe_id: int, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    fav = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.recipe_id == recipe_id).first()
    if not fav:
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(fav)
    db.commit()
    return

@router.post("/api/recipes/{recipe_id}/reviews", status_code=201, response_model=ReviewOut)
def add_review(recipe_id: int, review: ReviewCreate, db: Session = Depends(get_db), user_id: str = Depends(get_current_user)):
    new_review = Review(user_id=user_id, recipe_id=recipe_id, rating=review.rating, comment=review.comment)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/api/recipes/{recipe_id}/reviews", response_model=List[ReviewOut])
def get_reviews(recipe_id: int, db: Session = Depends(get_db)):
    reviews = db.query(Review).filter(Review.recipe_id == recipe_id).all()
    return reviews