import pytest
from unittest.mock import Mock, patch
from src.services.openai_service import OpenAIService

@pytest.fixture
def mock_openai():
    with patch('src.services.openai_service.OpenAI') as mock:
        yield mock

@pytest.fixture
def service(mock_openai):
    with patch.dict('os.environ', {'OPENAI_API_KEY': 'test-key'}):
        return OpenAIService()

def test_init_without_api_key():
    with patch.dict('os.environ', {}, clear=True):
        with pytest.raises(ValueError) as exc:
            OpenAIService()
        assert str(exc.value) == "OPENAI_API_KEY not found in environment variables"

def test_get_random_style(service):
    # Test multiple times to ensure randomness
    styles = set()
    for _ in range(50):
        style = service.get_random_style()
        styles.add(style)
        assert style in service.conversation_styles
    # Ensure we got at least 3 different styles
    assert len(styles) > 2

def test_get_chat_response_success(service, mock_openai):
    # Mock the OpenAI response
    mock_response = Mock()
    mock_response.choices = [Mock(message=Mock(content="Test response"))]
    service.client.chat.completions.create.return_value = mock_response
    
    # Mock the random style to ensure consistent testing
    fixed_style = "You are a helpful assistant"
    with patch.object(service, 'get_random_style', return_value=fixed_style):
        response = service.get_chat_response("Test message")
        
        assert response == "Test response"
        service.client.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": fixed_style},
                {"role": "user", "content": "Test message"}
            ]
        )

def test_get_chat_response_error(service, mock_openai):
    # Mock an error response
    service.client.chat.completions.create.side_effect = Exception("API Error")

    with pytest.raises(Exception) as exc:
        service.get_chat_response("Test message")
    assert str(exc.value) == "Error getting response from OpenAI: API Error"