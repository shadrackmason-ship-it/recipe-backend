from fastapi import FastAPI
from app.database import Base
from app.database import engine
from app.models.recipe import Recipe
from routes.recipes import router as recipe_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recipe_router)

@app.get("/")
def home():
    return {"message": "backend running"}