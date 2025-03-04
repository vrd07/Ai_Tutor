# backend/tests/test_integration.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
from app.models import models

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students/",
        json={"name": "Test Student", "level": "Beginner"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Student"
    assert data["level"] == "Beginner"
    assert "id" in data

def test_create_session():
    # First create a student
    student_response = client.post(
        "/students/",
        json={"name": "Another Student", "level": "Intermediate"}
    )
    student_id = student_response.json()["id"]
    
    # Create a session for this student
    response = client.post(
        "/sessions/",
        json={"student_id": student_id, "topic": "Python basics"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["student_id"] == student_id
    assert data["topic"] == "Python basics"
    assert "id" in data