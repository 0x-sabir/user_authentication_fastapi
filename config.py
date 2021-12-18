import os
from dotenv import load_dotenv

load_dotenv(dotenv_path = ".env")


class Setting:

    MYSQL_USER: str = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    MYSQL_SERVER: str = os.getenv("MYSQL_SERVER")
    MYSQL_PORT: str = os.getenv("MYSQL_PORT")
    MYSQL_DB: str = os.getenv("MYSQL_DB")
    DATABASE_URL:str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_SERVER}:{MYSQL_PORT}/{MYSQL_DB}"
    # DATABASE_URL:str = os.getenv("DATABASE_URL")
    ALGORITHM = "HS256"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    # ACCESS_TOKEN_EXPIRE_MINUTES: str  = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES",30)
    TEST_EMAIL: str = "test1@test.com"
    TEST_PASS: str = "test1pass"


settings = Setting()