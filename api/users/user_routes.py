from fastapi import APIRouter, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId
from ..db import get_db

router = APIRouter()

@router.get("/users")
def get_users(db = Depends(get_db)):
    return list(db["users"].find())

@router.post("/users")
def create_user(name: str, status: int, db = Depends(get_db)):
    new_user = {"name": name, "status": status}
    result = db["users"].insert_one(new_user)
    new_user["_id"] = str(result.inserted_id)
    return new_user

@router.get("/users/{userid}")
def get_user(userid: str, db = Depends(get_db)):
    return db["users"].find_one({"_id": ObjectId(userid)})

@router.put("/users/{userid}")
def update_user(userid: str, name: str, status: int, db = Depends(get_db)):
    db["users"].update_one({"_id": ObjectId(userid)}, {"$set": {"name": name, "status": status}})
    return db["users"].find_one({"_id": ObjectId(userid)})

@router.delete("/users/{userid}")
def delete_user(userid: str, db = Depends(get_db)):
    db["users"].delete_one({"_id": ObjectId(userid)})
    return {"deleted": userid}