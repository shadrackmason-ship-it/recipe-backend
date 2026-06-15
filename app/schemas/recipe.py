from pydantic import BaseModel, Field
from typing import List

class RecipeCreate(BaseModel):
    title: str = Field(min_length=2, max_length=100)
    description: str = Field(min_length=5)
    category: str
    prep_time: int = Field(gt=0)
    cook_time: int = Field(gt=0)
    servings: int = Field(gt=0)
    ingredients: List[str] = Field(default_factory=list)
    instructions: List[str] = Field(default_factory=list)

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    prep_time: int
    cook_time: int
    servings: int
    ingredients: list[str]
    instructions: list[str]
    class Config:
        from_attributes = True

class RecipeListResponse(BaseModel):
    page: int
    limit: int
    total: int
    data: list[RecipeResponse]