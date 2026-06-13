from fastapi import FastAPI
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from routes import community
from app.database import Base, engine
from app.models.community import Favorite, Review

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    print("Database tables created")

app.include_router(community.router)