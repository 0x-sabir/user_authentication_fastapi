from pydantic import BaseModel,EmailStr,UUID4,validator


class UserBase(BaseModel):
    email:EmailStr


class UserCreate(UserBase): 
    password:str
    confirm_password:str


class User(UserBase):
    id:UUID4 
    is_active:bool 

    class Config:
        orm_mode = True    


class LoginBase(BaseModel):
    username:EmailStr
    password:str

    class Config:
        orm_mode = True
        