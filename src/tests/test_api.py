from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)

def test_add_endpoint():
    response = client.post("/add", json={"a": 1, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 3, "operation": "add"}

def test_subtract_endpoint():
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2, "operation": "subtract"}

def test_multiply_endpoint():
    response = client.post("/multiply", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"result": 12, "operation": "multiply"}

def test_divide_endpoint():
    response = client.post("/divide", json={"a": 8, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result": 4.0, "operation": "divide"}

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 5, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"detail": "Cannot divide by zero"}
