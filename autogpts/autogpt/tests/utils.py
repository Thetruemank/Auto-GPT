import os

import pytest


def skip_in_ci(test_function):
    return pytest.mark.skipif(
        (os.environ.get("CI") == "true" or not os.environ.get("REQUIRED_ENV_VAR")),
        reason="This test doesn't work on GitHub Actions or necessary environment variables are not set.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
