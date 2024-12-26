import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c


def test_get_address_info(client):
    body = {"address": "TMKjYvLkGfKq2mZJuyEwHBRNSpMsmRz5yC"}
    client.headers["Content-Type"] = "application/json"
    response = client.post("/address_info/", json=body)
    assert response.status_code == 200
    data = response.json()
    assert data["address"] == "TMKjYvLkGfKq2mZJuyEwHBRNSpMsmRz5yC"
    assert isinstance(data["balance"], int)
    assert isinstance(data["energy"], int)
    assert isinstance(data["bandwidth"], int)


def test_read_requests(client):
    response = client.get("/requests/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["total"], int)
    assert isinstance(data["items"], list)