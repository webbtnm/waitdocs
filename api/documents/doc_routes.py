from fastapi import APIRouter, Depends
from pymongo import MongoClient
from bson.objectid import ObjectId
from ..db import get_db

router = APIRouter()

@router.get("/documents")
def get_documents(db = Depends(get_db)):
    return list(db["documents"].find())

@router.post("/documents")
def create_document(userid: str, name: str, description: str, db = Depends(get_db)):
    doc = {"userid": userid, "name": name, "description": description}
    result = db["documents"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.get("/documents/{documentid}")
def get_document(documentid: str, db = Depends(get_db)):
    return db["documents"].find_one({"_id": ObjectId(documentid)})

@router.put("/documents/{documentid}")
def update_document(documentid: str, name: str, description: str, db = Depends(get_db)):
    db["documents"].update_one({"_id": ObjectId(documentid)}, {"$set": {"name": name, "description": description}})
    return db["documents"].find_one({"_id": ObjectId(documentid)})

@router.delete("/documents/{documentid}")
def delete_document(documentid: str, db = Depends(get_db)):
    db["documents"].delete_one({"_id": ObjectId(documentid)})
    return {"deleted": documentid}