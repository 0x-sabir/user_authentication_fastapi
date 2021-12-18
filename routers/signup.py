from fastapi import HTTPException, Depends, APIRouter
from mydb import database,models,schemas, crud 
from mydb.hashing import Hash
from sqlalchemy.orm import Session
from pydantic import ValidationError


router = APIRouter()



@router.post("/users/faculty_signup/",response_model =schemas.User)
async def create_user(request:schemas.UserCreate,db:Session = Depends(database.get_db)):
    
    db_user = crud.get_user_by_email(db,email = request.email)

    if db_user:
        raise HTTPException(status_code = 400, detail = "Email already exists...")


    if request.password != request.confirm_password:
        raise HTTPException(status_code=400,detail="password does not match")  

    return crud.create_user(db=db, user=request)   
    # add_user = models.User(email = request.email,hashed_password = Hash.get_password_hashed(request.password))
    # db.add(add_user)
    # db.commit()
    # db.refresh(add_user)

    # return add_user


