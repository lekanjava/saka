"""
Test module for the FastAPI application.
"""
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """
    Test the root endpoint to ensure it returns the correct response.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
