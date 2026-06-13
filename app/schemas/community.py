from pydantic import BaseModel, Field
from datetime import datetime

class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5")
    comment: str = Field(..., max_length=500)

class ReviewOut(BaseModel):
    id: int
    rating: int
    comment: str
    user_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class FavoriteOut(BaseModel):
    recipe_id: int
    created_at: datetime
    class Config:
        from_attributes = True