from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ReviewCreate(BaseModel):
    rating: int = Field(..., ge=1, le=5, description="Rating from 1 to 5")
    comment: Optional[str] = Field(None, max_length=500) # Make this Optional

class ReviewOut(BaseModel):
    id: int
    rating: int
    comment: Optional[str] = None
    user_id: str # Changed from int to str
    recipe_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class FavoriteOut(BaseModel):
    id: int
    user_id: str # Add this - you were missing it
    recipe_id: int
    created_at: datetime
    class Config:
        from_attributes = True