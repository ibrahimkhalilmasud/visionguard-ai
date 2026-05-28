import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ["DATABASE_URL"] = f"sqlite:///{Path(__file__).parent / 'test.db'}"

from app.db import Base, engine
from app.main import app

Base.metadata.create_all(bind=engine)

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_register_and_login():
    email = "admin@example.com"

    register = client.post(
        "/api/v1/auth/register",
        json={
            "email": email,
            "full_name": "Admin User",
            "password": "StrongPass123",
            "role": "super_admin",
        },
    )
    assert register.status_code in (201, 409)

    login = client.post("/api/v1/auth/login", json={"email": email, "password": "StrongPass123"})
    assert login.status_code == 200
    assert "access_token" in login.json()
