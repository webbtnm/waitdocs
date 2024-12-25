
from sqlalchemy import Column, Integer, String, ForeignKey
from ..db import Base

class Document(Base):
    __tablename__ = "documents"

    documentid = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("users.userid"))
    name = Column(String)
    description = Column(String)