"""API integration tests."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "NEXEAGENT" in response.json()["name"]


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "documents_count" in data


def test_list_documents():
    response = client.get("/api/documents")
    assert response.status_code == 200
    assert "documents" in response.json()


def test_chat_missing_key_behavior():
    response = client.post(
        "/api/chat",
        json={"message": "Hello", "use_rag": False},
    )
    # Without API key, expect 503; with key, 200
    assert response.status_code in (200, 503)
