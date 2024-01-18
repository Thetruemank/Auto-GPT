import os

import pytest


def skip_in_ci(test_function):
    # Asserts if tests should be skipped in the CI environment
    # This decorator can be applied to tests that do not function within GitHub Actions,
    # However, crucial tests for build verification should not be skipped
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
