from sqlalchemy import Column, Integer, String, DateTime, BigInteger
from database import Base
import datetime


class UploadedDocs(Base):
    __tablename__ = "uploaded_docs"

    id = Column(Integer, primary_key=True, index=True)
    # object_id is uuid generated in main
    object_id = Column(BigInteger, index=True)
    filename = Column(String, index=True)
    content_type = Column(String)
    thumbnail = Column(String) #path to thumbnail
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    

