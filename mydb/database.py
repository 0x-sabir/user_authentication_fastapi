from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
from typing import Generator
import pymysql


SQLALCHEMY_DATABASE_URL  = settings.DATABASE_URL


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()    
