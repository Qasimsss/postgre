from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import User
import models
from schemas import *
import schemas

def create_user(db:Session , user: UserCreate):
    db_user = User(name=user.name , email= user.email , roll_no=user.roll_no )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def read_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

async def update_user(db:Session , user_id:int ,user:User):
    db_user = db.query(User).filter(User.id==user_id).first()
    db_user.name = user.name
    db_user.email=user.email
    db_user.roll_no=user.roll_no
    db.commit()
    db.refresh(db_user)
    if not db_user:
        raise HTTPException(status_code=404 , detail="user not found!")
    return db_user 

def delete_user(db:Session , user_id:int):
    db_user = db.query(User).filter(User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404 , detail="user not found!")
    db.delete(db_user)
    db.commit()
    return db_user

