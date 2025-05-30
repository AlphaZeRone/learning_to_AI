from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .import model, schema
from .database import engine, get_db
from typing import List

model.Base.metadata.create_all(bind = engine)

app = FastAPI()

#Create User
@app.post("/users", response_model = schema.UserResponse)

def create_user(user: schema.UserCreate, db: Session = Depends(get_db)) :
    existing_user = db.query(model.UserDB).filter(model.UserDB.email == user.email).first()

    if existing_user:
        raise HTTPException(status_code = 400, detail = "Email already registered")
    
    
    db_user_orm = model.UserDB(
        email = user.email,
        password = user.password,
        firstname = user.firstname,
        lastname = user.lastname,
        is_activated = True
    )
    db.add(db_user_orm)
    db.commit()
    db.refresh(db_user_orm)
    return db_user_orm

#Get User
@app.get("/users/{user_id}", response_model = schema.UserResponse)

def get_user(user_id: int, db: Session = Depends(get_db)):
    db_get_user = db.query(model.UserDB).filter(model.UserDB.id == user_id).first()

    if db_get_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    
    return db_get_user

#Get Users
@app.get("/users", response_model = List[schema.UserResponse])

def get_users(db: Session = Depends(get_db)):
    db_get_users = db.query(model.UserDB).all()
    return db_get_users

#Update User
@app.put("/users/{user_id}", response_model = schema.UserResponse)

async def update_user(user_id: int, user: schema.UserCreate, db: Session = Depends(get_db)):
    db_update_user = db.query(model.UserDB).filter(model.UserDB.id == user_id).first()

    if db_update_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    
    for key, value in user.model_dump().items():
        setattr(db_update_user, key, value)

    db.commit()
    db.refresh(db_update_user)
    return db_update_user

#Delete User
@app.delete("/users/{user_id}", response_model = schema.UserResponse)

async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_delete_user = db.query(model.UserDB).filter(model.UserDB.id == user_id).first()

    if db_delete_user is None:
        raise HTTPException(status_code = 404, detail = "User not found")
    
    db.delete(db_delete_user)
    db.commit()
    return db_delete_user



