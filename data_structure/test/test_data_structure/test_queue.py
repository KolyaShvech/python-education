"""
Module test Queue. Implement test all method Queue.
"""
import pytest

from data_structure.data_structure.queue import Queue


@pytest.fixture
def queue_list():
    """
    Create fixture for queue_list.
    """
    some_queue = Queue(300)
    some_queue.enqueue(500)
    return some_queue


def test_enqueue(queue_list):
    """
    Check method test enqueue.
    """
    queue_list.enqueue(700)
    assert list(queue_list) == [700, 500, 300]


def test_dequeue(queue_list):
    """
    Check method test dequeue.
    """
    queue_list.dequeue()
    assert list(queue_list) == [300]


def test_peek(queue_list):
    """
    Check method test peek.
    """
    queue_list.peek()
    assert list(queue_list) == [500, 300]