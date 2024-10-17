# backend/tests/test_inventory.py

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app.main import app
from ..app.database import Base, get_db
from ..app.config import settings
from ..app.utils.security import get_password_hash
from ..app.models import User

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_inventory.db"

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

def setup_module(module):
    # Create a test user
    db = TestingSessionLocal()
    hashed_password = get_password_hash("testpassword")
    user = User(email="inventory_manager@example.com", hashed_password=hashed_password, role="inventory_manager")
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()

def test_create_inventory():
    # Login to get token
    response = client.post(
        "/auth/login",
        data={"username": "inventory_manager@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]

    # Create inventory item
    response = client.post(
        "/inventory/",
        json={
            "name": "Test Item",
            "quantity": 100,
            "price": 9.99,
            "supplier_id": 1
        },
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["quantity"] == 100
    assert response.json()["price"] == 9.99
    assert response.json()["supplier_id"] == 1

def test_read_inventory():
    # Login to get token
    response = client.post(
        "/auth/login",
        data={"username": "inventory_manager@example.com", "password": "testpassword"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]

    # Read inventory items
    response = client.get(
        "/inventory/",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1
