# backend/tests/test_auth.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app.main import app
from ..app.database import Base, get_db
from ..app.config import settings

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Create the test database
Base.metadata.create_all(bind=engine)

client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={"email": "testuser@example.com", "password": "password123", "role": "user"}
    )
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"
    assert "id" in response.json()

def test_login():
    response = client.post(
        "/auth/login",
        data={"username": "testuser@example.com", "password": "password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
