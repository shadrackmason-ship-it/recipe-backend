from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "sqlite:///./recipes.db"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, # connection of py and database
    connect_args={"check_same_thread":False}
    )
sessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)
Base = declarative_base()# parent class for tables
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
