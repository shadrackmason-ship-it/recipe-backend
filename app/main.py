from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.api.routes.auth import router as auth_router
from app.api.routes.recipes import router as recipes_router
from app.api.routes.search import router as search_router
from app.api.routes.categories import router as categories_router

app = FastAPI(title="Recipe Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(recipes_router)
app.include_router(search_router)
app.include_router(categories_router)
