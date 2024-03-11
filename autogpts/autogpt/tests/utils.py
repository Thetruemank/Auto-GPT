import os

import pytest


def skip_in_ci(test_function):
    return pytest.mark.skipif(
        os.environ.get("CI") == "true",
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
import traceback

def log_test_failure(func):
    """
    Decorator to log detailed error information for tests that fail in the CI environment.
    Can be used as both a decorator and a context manager.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if os.environ.get("CI") == "true":
                print(f"Test {func.__name__} failed in CI environment.")
                print("Error details:")
                print(str(e))
                print("Stack trace:")
                traceback.print_exc()
            raise  # Re-raise the exception to ensure the test fails as expected
    return wrapper

class LogTestFailureContext:
    """
    Context manager to log detailed error information for tests that fail in the CI environment.
    """
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and os.environ.get("CI") == "true":
            print("Test failed in CI environment.")
            print("Error details:")
            print(str(exc_val))
            print("Stack trace:")
            traceback.print_tb(exc_tb)
        return False  # Re-raise the exception to ensure the test fails as expected
