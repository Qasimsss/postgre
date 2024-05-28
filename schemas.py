from pydantic import BaseModel

class UserCreate (BaseModel):
    name: str
    roll_no: int 
    email: str
