from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from app.database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    servings = Column(Integer)