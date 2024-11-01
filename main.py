from fastapi import FastAPI
from database import SessionLocal, engine
import models
from sqlalchemy.orm import joinedload

models.Base.metadata.create_all(bind=engine)    

app = FastAPI()

@app.post("/users/")
def create_user(username: str, name: str, password: str):
    db = SessionLocal()
    user = models.User(username=username, name=name, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str = None, name: str = None, password: str = None):
    db = SessionLocal()
    user = db.query(models.User).get(user_id)
    if user:
        if username: user.username = username
        if name: user.name = name
        if password: user.password = password
        db.commit()
    db.close()
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(models.User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
    db.close()
    return user

@app.post("/recipes/")
def create_recipe(title: str, instructions: str, user_id: int, nation_id: int, category_id: int, difficulty_id: int):
    db = SessionLocal()
    recipe = models.Recipe(title=title, instructions=instructions, user_id=user_id, nation_id=nation_id, category_id=category_id, difficulty_id=difficulty_id)
    db.add(recipe)
    db.commit()
    db.refresh(recipe)
    db.close()
    return recipe

@app.get("/recipes/{recipe_id}")
def get_recipe(recipe_id: int):
    db = SessionLocal()
    recipe = db.query(models.Recipe).get(recipe_id)
    db.close()
    return recipe

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, title: str = None, instructions: str = None):
    db = SessionLocal()
    recipe = db.query(models.Recipe).get(recipe_id)
    if recipe:
        if title: recipe.title = title
        if instructions: recipe.instructions = instructions
        db.commit()
    db.close()
    return recipe

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int):
    db = SessionLocal()
    recipe = db.query(models.Recipe).get(recipe_id)
    if recipe:
        db.delete(recipe)
        db.commit()
    db.close()
    return recipe

@app.post("/nations/")
def create_nation(name: str):
    db = SessionLocal()
    nation = models.Nation(name=name)
    db.add(nation)
    db.commit()
    db.refresh(nation)
    db.close()
    return nation

@app.get("/nations/{nation_id}")
def get_nation(nation_id: int):
    db = SessionLocal()
    nation = (db.query(models.Nation).options(joinedload(models.Nation.recipes)).get(nation_id))
    db.close()
    return nation

@app.get("/nations/{nation_id}")
def nation(nation_id: int):
    db = SessionLocal()
    nation = (db.query(models.Nation).get(nation_id))
    db.close()
    return nation

@app.put("/nations/{nation_id}")
def update_nation(nation_id: int, name: str):
    db = SessionLocal()
    nation = db.query(models.Nation).get(nation_id)
    if nation:
        nation.name = name
        db.commit()
    db.close()
    return nation

@app.delete("/nations/{nation_id}")
def delete_nation(nation_id: int):
    db = SessionLocal()
    nation = db.query(models.Nation).get(nation_id)
    if nation:
        db.delete(nation)
        db.commit()
    db.close()
    return nation

@app.post("/categories/")
def create_category(name: str):
    db = SessionLocal()
    category = models.Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    db.close()
    return category

@app.get("/categories/{category_id}")
def category(category_id: int):
    db = SessionLocal()
    category = db.query(models.Category).get(category_id)
    db.close()
    return category

@app.get("/categories/{category_id}")
def category_user(category_id: int):
    db = SessionLocal()
    category = db.query(models.Category).options(joinedload(models.Category.recipes)).get(category_id)
    db.close()
    return category

@app.put("/categories/{category_id}")
def update_category(category_id: int, name: str):
    db = SessionLocal()
    category = db.query(models.Category).get(category_id)
    if category:
        category.name = name
        db.commit()
    db.close()
    return category

@app.delete("/categories/{category_id}")
def delete_category(category_id: int):
    db = SessionLocal()
    category = db.query(models.Category).get(category_id)
    if category:
        db.delete(category)
        db.commit()
    db.close()
    return category

@app.post("/difficulties/")
def create_diff(level: str):
    db = SessionLocal()
    diff = models.Difficulty(level=level)
    db.add(diff)
    db.commit()
    db.refresh(diff)
    db.close()
    return diff

@app.get("/difficulties/{difficulty_id}")
def diff(difficulty_id: int):
    db = SessionLocal()
    diff = db.query(models.Difficulty).get(difficulty_id)
    db.close()
    return diff

@app.get("/difficulties/{difficulty_id}")
def diff_user(difficulty_id: int):
    db = SessionLocal()
    diff = db.query(models.Difficulty).options(joinedload(models.Difficulty.recipes)).get(difficulty_id)
    db.close()
    return diff

@app.put("/difficulties/{difficulty_id}")
def update_diff(difficulty_id: int, level: str):
    db = SessionLocal()
    diff = db.query(models.Difficulty).get(difficulty_id)
    if diff:
        diff.level = level
        db.commit()
    db.close()
    return diff

@app.delete("/difficulties/{difficulty_id}")
def delete_dif(difficulty_id: int):
    db = SessionLocal()
    diff = db.query(models.Difficulty).get(difficulty_id)
    if diff:
        db.delete(diff)
        db.commit()
    db.close()
    return diff
