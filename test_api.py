import pytest

from fastapi.testclient import TestClient
from main import app
from tortoise import Tortoise, run_async
from main import User
import time

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

    await User.create(username=username1, password_hash="hashed_password_1")
    await User.create(username=username2, password_hash="hashed_password_2")


# Fixture to initialize test database and add test data before tests
def setup_function():
    run_async(init_test_db())
    run_async(add_test_data())


# Test case to check if the server responds with a 200 status code for getusers route
def test_get_users():
    response = client.get("/getusers")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 2


# Teardown function to clean up the database after tests
def teardown_function():
    run_async(Tortoise.close_connections())
