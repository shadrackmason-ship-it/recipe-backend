from fastapi import FastAPI
from app.api.routes import search, categories

app = FastAPI()

app.include_router(search.router)
app.include_router(categories.router)