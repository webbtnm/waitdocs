
from sqlalchemy import Column, Integer, String
from ..db import Base

class User(Base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(Integer)