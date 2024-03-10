import os
import sys

import pytest
from autogpts.autogpt.tests.utils import skip_in_ci


def test_python_version():
    assert sys.version_info >= (3, 10), "Python version must be at least 3.10"

def test_environment_variables():
    required_vars = ["CI", "HOME"]
    for var in required_vars:
        assert var in os.environ, f"{var} environment variable is required"

def test_dependencies_installed():
    try:
        import autogpt
        import click
        import pytest
    except ImportError as e:
        pytest.fail(str(e))
