import os

import pytest


def skip_in_ci(test_function):
    if os.environ.get("CI") == "true":
        print(f"Skipping {test_function.__name__} due to running in GitHub Actions CI environment.")
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
