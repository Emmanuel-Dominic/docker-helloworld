import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.app_context():
        with app.test_client() as client:
            yield client

def test_hello(client):
    rv = client.get('/')
    assert True
    assert b'Hello World!' in rv.data
    assert rv.status_code == 200
