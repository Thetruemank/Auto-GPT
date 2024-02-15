import os
from unittest.mock import MagicMock, patch

import pytest
from autogpts.autogpt.tests.utils import skip_in_ci
from cli import check_github_token, configure_github_credentials
from frontend.lib.services.auth_service import AuthService


@pytest.fixture
def mock_auth_service():
    with patch('frontend.lib.services.auth_service.GithubAuthProvider') as mock_auth_provider:
        yield AuthService()

@pytest.fixture
def mock_cli_functions():
    with patch('cli.requests.get') as mock_get, patch('cli.click.echo') as mock_echo:
        mock_get.return_value = MagicMock(status_code=200, headers={'X-OAuth-Scopes': 'repo'})
        yield mock_get, mock_echo

@skip_in_ci
def test_github_authentication_success(mock_auth_service):
    with patch.dict(os.environ, {'GITHUB_ACTIONS': 'true'}), patch('frontend.lib.services.auth_service._auth.signInWithPopup') as mock_sign_in:
        mock_sign_in.return_value = MagicMock(user="TestUser")
        assert mock_auth_service.signInWithGitHub() is not None

@skip_in_ci
def test_github_authentication_failure(mock_auth_service):
    with patch.dict(os.environ, {'GITHUB_ACTIONS': 'true'}), patch('frontend.lib.services.auth_service._auth.signInWithPopup', side_effect=Exception("Auth Failed")):
        assert mock_auth_service.signInWithGitHub() is None

@skip_in_ci
def test_github_api_interaction_success(mock_cli_functions):
    mock_get, _ = mock_cli_functions
    assert check_github_token("valid_token") is True

@skip_in_ci
def test_github_api_interaction_failure_due_to_permissions(mock_cli_functions):
    mock_get, mock_echo = mock_cli_functions
    mock_get.return_value.headers = {'X-OAuth-Scopes': ''}
    check_github_token("invalid_scope_token")
    mock_echo.assert_called_with(pytest.any, fg="red")

@skip_in_ci
def test_github_api_interaction_failure_due_to_invalid_token(mock_cli_functions):
    mock_get, mock_echo = mock_cli_functions
    mock_get.return_value.status_code = 401
    check_github_token("invalid_token")
    mock_echo.assert_called_with(pytest.any, fg="red")
