import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_say_hello():
    response = client.get("/hello/testuser")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello testuser"}

def test_iterate():
    grid = {
        "grid": [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
    }
    response = client.post("/iterate", json=grid)
    assert response.status_code == 200
    assert "grid" in response.json()

def test_iterate100():
    grid = {
        "grid": [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
    }
    response = client.post("/iterate100", json=grid)
    assert response.status_code == 200
    assert "grid" in response.json()

def test_iterate1000():
    grid = {
        "grid": [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1]
        ]
    }
    response = client.post("/iterate1000", json=grid)
    assert response.status_code == 200
    assert "grid" in response.json()

def test_large_grid1000():
    # Create a large grid (e.g., 1000x1000)
    size = 1000
    large_grid = {
        "grid": [[0 for _ in range(size)] for _ in range(size)]
    }
    response = client.post("/iterate1000", json=large_grid)
    assert response.status_code == 200
    assert "grid" in response.json()
    assert len(response.json()["grid"]) == size
    assert len(response.json()["grid"][0]) == size