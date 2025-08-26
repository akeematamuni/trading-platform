from api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_home():
    res = client.get("/home")
    assert res.status_code == 200

    data = res.json()
    assert data["message"] == "api"
