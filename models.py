from sqlalchemy import Integer , String ,  Column
from database import Base


class User(Base):
    __tablename__="users"
    id = Column(Integer , primary_key=True ,index=True)
    name = Column(String , index=True)
    roll_no = Column(Integer , unique=True , index=True)
    email = Column(String , index =True , unique=True)
