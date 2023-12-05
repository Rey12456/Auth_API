import pytest

from fastapi.testclient import TestClient
from main import app
from tortoise import Tortoise, run_async
from main import User
import time
from main import JWT_SECRET
import jwt
import bcrypt

client = TestClient(app)


# Initialize Tortoise with the test database
async def init_test_db():
    await Tortoise.init(
        db_url="sqlite://db_test.sqlite3",  # Test database URL
        modules={"models": ["main"]},  # Path to your models
    )
    await Tortoise.generate_schemas()


async def add_test_data():
    await User.all().delete()
    username1 = "Jah"
    username2 = "Morant"
    password_hash1 = bcrypt.hashpw(b"123", bcrypt.gensalt())  
    password_hash2 = bcrypt.hashpw(b"321", bcrypt.gensalt())  

    await User.create(username=username1, password_hash=password_hash1.decode("utf-8"))
    await User.create(username=username2, password_hash=password_hash2.decode("utf-8"))


def setup_function():
    run_async(init_test_db())
    run_async(add_test_data())


# Test case to check if the server responds with a 200 status code for getusers route
def test_get_users():
    response = client.get("/getusers")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 2

def test_generate_token_valid_credentials():
    # Prepare test user data
    test_user = {
        "username": "Jah",
        "password": "123",
    }

    # Generate token using the test user's credentials
    response = client.post("/token", data=test_user)

    # Assert the token generation is successful (status code 200)
    assert response.status_code == 200
    assert "Access token" in response.json()
    

# Teardown function to clean up the database after tests
def teardown_function():
    run_async(Tortoise.close_connections())
