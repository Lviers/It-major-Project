from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    password = Column(String)

    recipes = relationship("Recipe", back_populates="user")

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    instructions = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    nation_id = Column(Integer, ForeignKey('nations.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    difficulty_id = Column(Integer, ForeignKey('difficulties.id'))

    user = relationship("User", back_populates="recipes")
    nation = relationship("Nation", back_populates="recipes")
    category = relationship("Category", back_populates="recipes")
    difficulty = relationship("Difficulty", back_populates="recipes")

class Nation(Base):
    __tablename__ = 'nations'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    recipes = relationship("Recipe", back_populates="nation")

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    recipes = relationship("Recipe", back_populates="category")

class Difficulty(Base):
    __tablename__ = 'difficulties'
    id = Column(Integer, primary_key=True, index=True)
    level = Column(String, unique=True)

    recipes = relationship("Recipe", back_populates="difficulty")
