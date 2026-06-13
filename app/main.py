from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth
Base.metadata.create_all(Bind=engine)
app = FastAPI(title="Recipe Backend")
app.include_router(auth.router)