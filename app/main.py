from fastapi import FastAPI
from app.database import Base, engine
from routes import auth


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Recipe Backend")

@app.get("/")
def root():
    return {"message": "Recipe backend is running"}

app.include_router(auth.router,prefix="/api")