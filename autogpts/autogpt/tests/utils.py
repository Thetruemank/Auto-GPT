import os

import pytest


def skip_in_ci(test_function):
    """
    Decorator to skip the execution of a test function in a CI environment.

    Use this decorator to tag test functions that should not be executed when the tests are run
    in a Continuous Integration (CI) system like GitHub Actions due to environment constraints
    or other reasons.

    Args:
        test_function: A test function that should be skipped in CI.

    Returns:
        The same test function marked to be skipped when the 'CI' environment variable is set to 'true'.
    """
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
