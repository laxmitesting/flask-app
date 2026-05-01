import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Tests the root / route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Weather API is running" in response.data

def test_weather_route_default(client):
    """Tests the /weather route returns JSON with current weather"""
    response = client.get('/weather')
    assert response.status_code == 200
    data = response.get_json()
    assert "temperature" in data
    assert "windspeed" in data