
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db import SessionLocal
from .doc_models import Document

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    return db.query(Document).all()

@router.post("/documents")
def create_document(userid: int, name: str, description: str, db: Session = Depends(get_db)):
    doc = Document(userid=userid, name=name, description=description)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/documents/{documentid}")
def get_document(documentid: int, db: Session = Depends(get_db)):
    return db.query(Document).filter(Document.documentid == documentid).first()

@router.put("/documents/{documentid}")
def update_document(documentid: int, name: str, description: str, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.documentid == documentid).first()
    if doc:
        doc.name = name
        doc.description = description
        db.commit()
        db.refresh(doc)
    return doc

@router.delete("/documents/{documentid}")
def delete_document(documentid: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.documentid == documentid).first()
    if doc:
        db.delete(doc)
        db.commit()
    return {"deleted": documentid}