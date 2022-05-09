"""
Module test Stack. Implement all methods from Stack class.
"""
import pytest

from data_structure.data_structure.stack import Stack


@pytest.fixture
def stack_list():
    """
    Create fixture for stack_list.
    """
    some_stack = Stack(10)
    some_stack.push(20)
    return some_stack


def test_push(stack_list):
    """
    Check method test push.
    """
    stack_list.push(30)
    assert list(stack_list) == [30, 20, 10]


def test_pop(stack_list):
    """
    Check method test pop.
    """
    stack_list.pop()
    assert list(stack_list) == [20]


def test_peek(stack_list):
    """
    Check method test peek.
    """
    stack_list.peek()
    assert list(stack_list) == [20, 10]
