import pytest 
from fastapi.testclient import TestClient
from authorization import token
from main import app

client = TestClient(app)


def test_authentication():
    response = client.post(
        "/users/login/",
        json = {
    "username":"deadpool76@gmail.com",
    "password":"HelloKalu"
    }
    )
    assert response.status_code == 200,response.text
    data = response.json()


     
    
