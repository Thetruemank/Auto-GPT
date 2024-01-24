import os

import pytest


def skip_in_ci(test_function):
    return pytest.mark.skipif(
        (os.environ.get("CI") == "true" or os.environ.get("SKIP_EXTERNAL_TESTS") == "true" or "notsuitableforci" in test_function.keywords),
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
