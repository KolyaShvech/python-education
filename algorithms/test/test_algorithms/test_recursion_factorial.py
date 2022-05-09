"""
Module test recursion factorial.
"""
import pytest

from algorithms_code.recurtion_factorial import recursion_factorial


@pytest.fixture
def re_factorial():
    """
    Create fixture to recursion_factorial.
    """
    return recursion_factorial(5)


@pytest.mark.parametrize("data, expected", [
    (5, 120),
    (6, 720),
    (10, 3628800),
])


def test_recursion_factorial(re_factorial, data, expected):
    """
    Apply parametrize.
    """
    actual_result = recursion_factorial(data)
    assert actual_result == expected
