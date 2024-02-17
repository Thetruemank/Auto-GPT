import os

import pytest


def skip_unless_in_ci(test_function):
    return pytest.mark.skipif(
        not (os.environ.get("CI") == "true" or os.environ.get("GITHUB_ACTIONS") == "true"),
        reason="This test is intended to run only in CI environments.",
    )(test_function)
