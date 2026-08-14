from fastapi.testclient import TestClient

from cloud_devops_pr import app

client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Cloud DevOps CI/CD - test version (demo)",
        "version": "0.1.0",
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
