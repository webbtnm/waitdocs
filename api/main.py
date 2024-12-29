from fastapi import FastAPI
from .db import get_db
from .users.user_routes import router as user_router
from .documents.doc_routes import router as doc_router

app = FastAPI()

# Remove SQLAlchemy initialization
# Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(doc_router)