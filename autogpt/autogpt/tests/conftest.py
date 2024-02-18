from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(scope="function")
def test_environment():
    # Setup phase: Initialize necessary variables or states
    original_state = "original state"
    modified_state = "modified for test"
    
    # Yield control back to the test function
    yield modified_state
    
    # Teardown phase: Revert any modifications to ensure a clean state
    modified_state = original_state

@pytest.fixture(scope="module")
def mock_github_api():
    with patch("github.Github") as mock_github:
        mock_instance = MagicMock()
        mock_instance.get_user.return_value = MagicMock(login="test_user", id=12345)
        mock_instance.get_repo.return_value = MagicMock(name="test_repo", id=67890)
        mock_instance.get_issues.return_value = [MagicMock(title="Issue 1", id=111), MagicMock(title="Issue 2", id=222)]
        
        mock_github.return_value = mock_instance
        yield mock_github
