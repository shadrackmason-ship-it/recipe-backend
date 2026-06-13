from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class Favorite(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    recipe_id = Column(Integer, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    recipe_id = Column(Integer, index=True)
    rating = Column(Integer)
    comment = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())