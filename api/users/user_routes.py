
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .user_models import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/users")
def create_user(name: str, status: int, db: Session = Depends(get_db)):
    new_user = User(name=name, status=status)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/users/{userid}")
def get_user(userid: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.userid == userid).first()

@router.put("/users/{userid}")
def update_user(userid: int, name: str, status: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.userid == userid).first()
    if user:
        user.name = name
        user.status = status
        db.commit()
        db.refresh(user)
    return user

@router.delete("/users/{userid}")
def delete_user(userid: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.userid == userid).first()
    if user:
        db.delete(user)
        db.commit()
    return {"deleted": userid}