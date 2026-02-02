import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home(client):
    """Verify the home page loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps Pipeline is Active!" in response.data
