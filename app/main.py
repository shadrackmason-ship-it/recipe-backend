from fastapi import FastAPI
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


from app.api.routes.auth import router as auth_router
from app.api.routes.recipes import router as recipes_router   
from app.api.routes.search import router as search_router
from app.api.routes.categories import router as categories_router

app = FastAPI(title="Recipe Backend")

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "https://fabulous-beijinho-cce89f.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(recipes_router)
app.include_router(search_router)
app.include_router(categories_router)
