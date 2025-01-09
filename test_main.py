"""
Test module for the FastAPI application.
"""
from fastapi.testclient import TestClient
import os
from main import app

client = TestClient(app)

def test_static_files_exist():
    """
    Test that required static files exist
    """
    assert os.path.exists("static/index.html"), "index.html is missing"

def test_read_root():
    """
    Test the root endpoint to ensure it returns the HTML file
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")  # Check if it returns HTML

def test_analyze_password():
    """
    Test the password analysis endpoint
    """
    response = client.post(
        "/analyze-password",
        json={"password": "Test123!@#"}
    )
    assert response.status_code == 200
    result = response.json()
    assert "strength" in result
    assert "feedback" in result
    assert "timeToHack" in result
