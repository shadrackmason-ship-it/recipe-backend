from fastapi import FastAPI
from routes.recipes import router as recipe_router

app = FastAPI()

app.include_router(recipe_router)

@app.get("/")
def home():
    return {"message": "backend running"}