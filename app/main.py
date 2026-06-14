from fastapi import FastAPI
from app.database import Base, engine
from routes import auth
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.search import router as search_router
from app.api.routes.categories import router as categories_router

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router)
app.include_router(categories_router)
