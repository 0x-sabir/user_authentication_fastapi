from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(data, credentials_exception)



##NOTE: while authorization use the Header Authorization, with a value that starts with Bearer e.g:- Header:Authorization,value: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJjaGVja2F1dGhAZ21haWwuY29tIiwiZXhwIjoxNjM4OTU0MDYwfQ.qL44NjsTq8r68vJDHi2JFoDQBBQemUt09d1m-G