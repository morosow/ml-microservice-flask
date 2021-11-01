import pytest
import sys

from app import application


@pytest.fixture
def client():
    with application.test_client() as c:
        yield c


def test_health_check(client) -> None:
    response = client.get('/health')
    assert response.status_code == 200
