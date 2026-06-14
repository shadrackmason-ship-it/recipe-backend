from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base
from app.database import engine
from app.models.recipe import Recipe
from routes.recipes import router as recipe_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe_router)

@app.get("/")
def home():
    return {"message": "backend running"}