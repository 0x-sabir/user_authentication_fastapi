import pytest 
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from mydb.database import Base,get_db
from main import app
from config import settings
# from typing import Generator,Any
import pymysql



SQLALCHEMY_DATABASE_URL  = settings.DATABASE_URL

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:Sabir123@localhost:3306/Users"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

@pytest.fixture
async def override_get_db():
    try:
      db = TestingSessionLocal()
      yield db  
    finally:
        db.close()    

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

# @pytest.fixture
# def client() -> Generator[TestClient, Any, None]:
#     def override_get_db():
#         try:
#             db = TestingSessionLocal()
#             yield db
#         finally:
#             db.close()

#     app.dependency_overrides[get_db] = override_get_db
#     client = TestClient(app)
#     yield client




def test_create_user():
    response = client.post(
        "/users/signup/",
        json = {"email":"deadpool76@gmail.com","password":"HelloKalu","confirm_password":"HelloKalu"},
    )

    assert response.status_code == 200 , response.text
    data = response.json()
    assert data["email"] == "deadpool76@gmail.com"
    assert "id" in data
    user_id = data["id"]

    # reponse = client.get(f"/get_user")

    
    # assert reponse.status_code == 200,reponse.text
    # data = reponse.json()
    # assert data["email"] == "deadpool@gmail.com"
    # assert data["id"] == user_id
