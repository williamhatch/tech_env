#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for FastAPI application
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from src.app import app
from src.database import Base, get_db
from src.models import Item


# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Override the get_db dependency
def override_get_db():
    """
    Override the database dependency for testing
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def test_client():
    """
    Create a test client for the FastAPI application
    
    Returns:
        TestClient: FastAPI test client
    """
    # Create the database tables
    Base.metadata.create_all(bind=engine)
    
    # Create a test client
    client = TestClient(app)
    
    # Return the test client
    yield client
    
    # Clean up the database
    Base.metadata.drop_all(bind=engine)


def test_read_root(test_client):
    """
    Test the root endpoint
    
    Args:
        test_client: FastAPI test client
    """
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Interview API"}


def test_create_item(test_client):
    """
    Test creating an item
    
    Args:
        test_client: FastAPI test client
    """
    # Create an item
    response = test_client.post(
        "/items/",
        json={"name": "Test Item", "description": "This is a test item"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["description"] == "This is a test item"
    assert data["is_active"] is True
    assert "id" in data
    assert "created_at" in data


def test_read_items(test_client):
    """
    Test reading all items
    
    Args:
        test_client: FastAPI test client
    """
    # Create some items
    test_client.post("/items/", json={"name": "Item 1"})
    test_client.post("/items/", json={"name": "Item 2"})
    
    # Get all items
    response = test_client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Item 1"
    assert data[1]["name"] == "Item 2"


def test_read_item(test_client):
    """
    Test reading a specific item
    
    Args:
        test_client: FastAPI test client
    """
    # Create an item
    response = test_client.post("/items/", json={"name": "Test Item"})
    item_id = response.json()["id"]
    
    # Get the item
    response = test_client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Item"
    assert data["id"] == item_id


def test_read_item_not_found(test_client):
    """
    Test reading a non-existent item
    
    Args:
        test_client: FastAPI test client
    """
    response = test_client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_delete_item(test_client):
    """
    Test deleting an item
    
    Args:
        test_client: FastAPI test client
    """
    # Create an item
    response = test_client.post("/items/", json={"name": "Item to Delete"})
    item_id = response.json()["id"]
    
    # Delete the item
    response = test_client.delete(f"/items/{item_id}")
    assert response.status_code == 204
    
    # Try to get the deleted item
    response = test_client.get(f"/items/{item_id}")
    assert response.status_code == 404
