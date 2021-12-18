########################### HASHING PASSWORD & VERIFYING IT  ################################

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def get_password_hashed(password: str):
        return pwd_context.hash(password)

    def verify_hash_password(hashed_password,plain_password):
        return  pwd_context.verify(plain_password,hashed_password)
