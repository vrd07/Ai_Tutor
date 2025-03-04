# backend/tests/test_llm_service.py
import pytest
from app.services.llm_service import LLMService
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_generate_lesson():
    with patch('app.services.llm_service.httpx.AsyncClient') as mock_client:
        # Setup mock response
        mock_response = AsyncMock()
        mock_response.json.return_value = {"response": "Test lesson content"}
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        # Test the service
        service = LLMService()
        result = await service.generate_lesson("Python", "Beginner")
        
        # Assertions
        assert result == "Test lesson content"
        mock_client.return_value.__aenter__.return_value.post.assert_called_once()
        
@pytest.mark.asyncio
async def test_generate_quiz():
    with patch('app.services.llm_service.httpx.AsyncClient') as mock_client:
        # Setup mock response
        mock_response = AsyncMock()
        mock_response.json.return_value = {"response": "Test quiz content"}
        mock_client.return_value.__aenter__.return_value.post.return_value = mock_response
        
        # Test the service
        service = LLMService()
        result = await service.generate_quiz("Lesson about Python")
        
        # Assertions
        assert result == "Test quiz content"
        mock_client.return_value.__aenter__.return_value.post.assert_called_once()