import pytest 
from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)


def test_signup():
    response = client.post(
        "/users/signup/",
        json = {"email":"dead6977@gmail.com","password":"fuckyou","confirm_password":"fuckyou"},
    )

    assert response.status_code == 200 , response.text
    data = response.json()
    assert data["email"] == "dead6977@gmail.com"
    assert "id" in data
    user_id = data["id"]
