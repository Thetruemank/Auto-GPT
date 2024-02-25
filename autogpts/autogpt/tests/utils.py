import os

import pytest


# This decorator is used to skip certain tests when running in a Continuous Integration (CI) environment like GitHub Actions.
# Skipping tests can be necessary for cases where tests require specific environment configurations not available in CI.
def skip_in_ci(test_function):
    print(f"Skipping {test_function.__name__} in CI environment.")
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
