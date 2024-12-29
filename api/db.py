from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

client = MongoClient(DATABASE_URL)
db = client.get_database()

def get_db():
    try:
        yield db
    finally:
        client.close()