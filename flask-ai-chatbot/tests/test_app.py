import pytest
from unittest.mock import patch, Mock
from src.app import app
from src.services.openai_service import OpenAIService

@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def mock_openai_service():
    """Mock the OpenAI service"""
    with patch('src.app.openai_service') as mock:
        mock.get_chat_response.return_value = "Test response"
        yield mock

def test_index_route(client):
    """Test the index route returns 200 and renders index.html"""
    response = client.get('/')
    assert response.status_code == 200

def test_chat_route(client):
    """Test the chat route returns 200 and renders chat.html"""
    response = client.get('/chat')
    assert response.status_code == 200

def test_api_chat_success(client, mock_openai_service):
    """Test successful chat API request"""
    # Set up mock response
    mock_openai_service.get_chat_response.return_value = "Test response"
    
    response = client.post('/api/chat', 
                         json={'message': 'Test message'},
                         content_type='application/json')
    
    assert response.status_code == 200
    assert response.get_json() == {'response': 'Test response'}
    
    # Verify mock was called correctly
    mock_openai_service.get_chat_response.assert_called_once_with('Test message')

def test_api_chat_missing_message(client):
    """Test chat API request without message"""
    response = client.post('/api/chat', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'No message provided'}

def test_api_chat_error(client, mock_openai_service):
    """Test chat API request with service error"""
    # Mock the OpenAI service to raise an exception
    mock_openai_service.get_chat_response.side_effect = Exception("Test error")

    response = client.post('/api/chat', json={'message': 'Test message'})
    
    assert response.status_code == 500
    assert response.json == {'error': 'Test error'}