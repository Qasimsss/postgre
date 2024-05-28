from fastapi import FastAPI , Depends , HTTPException
from database import *
from schemas import *
from sqlalchemy.orm import Session
from crud import *
import schemas
import crud

app = FastAPI()

Base.metadata.create_all(bind = engine )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/user/create" , response_model=schemas.UserCreate)
async def create_user_api(user : UserCreate , db:Session=Depends(get_db)):
    return create_user(db , user)
'''
@app.get("/users/{user_id}")
async def read_user(user_id: int , db:Session=Depends(get_db)):
    db_user=read_user(db , user_id)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404 , detail="user not found!")'''



@app.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = await crud.read_user(db, user_id)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="User not found")

"""
@app.post("/user/update" , response_model=schemas.UserCreate)
async def update_user_api(user_id:int , user : UserCreate , db:Session=Depends(get_db)):
    return update_user(db , user_id , user)
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404 , detail="user not found!")"""


@app.put("/user/update", response_model=schemas.UserCreate)
async def update_user_api(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        updated_user = await update_user(db, user_id, user)
        if updated_user:
            return updated_user
        else:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.delete("/user/delete" , response_model=schemas.UserCreate)
async def delete_user_api(user_id:int  , db:Session=Depends(get_db)):
    return delete_user(db , user_id )
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404 , detail="user not found!")