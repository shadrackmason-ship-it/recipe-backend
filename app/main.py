from fastapi import FastAPI
from app.database import Base, engine
from routes import auth

from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Recipe Backend")
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "Recipe backend is running"}

app.include_router(auth.router,prefix="/api")