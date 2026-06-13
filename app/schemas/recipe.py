from pydantic import BaseModel

class RecipeCreate(BaseModel):
    title: str
    description: str
    category: str
    prep_time: int
    cook_time: int
    servings: int

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    prep_time: int
    cook_time: int
    servings: int
    class Config:
        from_attributes = True