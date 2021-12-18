from fastapi import HTTPException, Depends, status, APIRouter 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from mydb import database,models,schemas 
from mydb.hashing import Hash
from sqlalchemy.orm import Session
from authorization import token

router = APIRouter()


@router.post("/login")
async def authenticate_user(request: schemas.LoginBase, db:Session = Depends(database.get_db)):

    db_user = db.query(models.User).filter(models.User.email == request.username ).first()


    if not db_user:
        raise HTTPException(status_code=401, detail='Invalid username')

    if not Hash.verify_hash_password(db_user.hashed_password,request.password):
        raise HTTPException(status_code=401, detail='Invalid password')

    access_token = token.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}




