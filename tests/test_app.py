import pytest
import sys
import os

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

from app import app

# setup a test client using pytest fixture
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Put Flask in test mode
    with app.test_client() as client:  # Create a fake browser
        yield client  # Give it to the tests e.g. passing "client" as argument

def test_home_endpoint(client):
    """Test that home endpoint returns 200 status"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_returns_json(client):
    """Test that home endpoint returns JSON"""
    response = client.get('/')
    json_data = response.get_json()
    assert 'status' in json_data
    assert 'hostname' in json_data
    assert 'timestamp' in json_data

def test_status_message(client):
    """Test that status message is correct"""
    response = client.get('/')
    json_data = response.get_json()
    assert json_data['status'] == 'Application is running'