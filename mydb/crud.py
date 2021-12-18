from fastapi import Depends
from sqlalchemy.orm import Session
from mydb import models,schemas,database
from mydb.hashing import Hash


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()



def create_user(db:Session,user: schemas.UserCreate):

    db_user =  models.User(email= user.email, hashed_password=  Hash.get_password_hashed(user.password))

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user