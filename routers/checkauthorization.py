from fastapi import HTTPException, Depends, status, APIRouter 
from mydb import database,models,schemas 
from sqlalchemy.orm import Session
from authorization import token,oauth2

router = APIRouter()

@router.get("/get_user")
async def get_myuser(request:schemas.User = Depends(oauth2.get_current_user),db:Session = Depends(database.get_db)):
    
    return {"Authorization":"successful"}
