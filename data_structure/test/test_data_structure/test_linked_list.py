"""
Module which implement test at linked list.
"""
from unittest.mock import patch

import pytest
from linkedlist.linked_list import LinkedList


@pytest.fixture
def some_linked_list():
    """
    Create fixture for Linked List.
    """
    llist = LinkedList(100)
    llist.append(150)
    return llist


def test_prepend(some_linked_list):
    """
    Check method test prepend.
    """
    some_linked_list.prepend(200)
    assert list(some_linked_list) == [200, 100, 150]


def test_append(some_linked_list):
    """
    Check method test append.
    """
    some_linked_list.append(500)
    assert list(some_linked_list) == [100, 150, 500]


@pytest.mark.parametrize('data, expected', [(150, 1), (200, None)])
def test_loot_up(some_linked_list, data, expected):
    """
    Check method test look up. Use parametrize.
    """
    actual = some_linked_list.look_up(data)
    assert actual == expected


@pytest.mark.parametrize('index, expected_list', [
    (0, [200, 100, 150]),
    (1, [100, 200, 150]),
    (2, [100, 150, 200])
])
def test_insert(some_linked_list, index, expected_list):
    """
    Check method test insert. Use  parametrize.
    """
    some_linked_list.insert(200, index)
    assert list(some_linked_list) == expected_list


@pytest.mark.parametrize("index", [-1, 3])
def test_insert_index_out_of_range(some_linked_list, index):
    """
    Check method test insert index out of range. Use  parametrize.
    """
    with pytest.raises(IndexError):
        some_linked_list.insert(200, index)


@patch('data_structure.linked_list.LinkedList._delete_first_arg')
def test_delete_by_first_index(mock_method, some_linked_list):
    """
    Check method test delete by first index. Use patch with mock_method.
    """
    some_linked_list.delete(0)
    mock_method.assert_called()


@patch('data_structure.linked_list.LinkedList._delete_arg_by_index')
def test_delete(mock_method, some_linked_list):
    """
    Check method test delete arg by first index. Use patch with mock_method.
    """
    some_linked_list.delete(1)
    mock_method.assert_called()


@pytest.mark.parametrize("index", [-1, 5])
def test_delete_by_index_out_of_range(some_linked_list, index):
    """
    Check method test delete be index out of range, raise IndexError.
    """
    with pytest.raises(IndexError):
        some_linked_list.delete(index)


@pytest.mark.parametrize("index, expected_list", [
    (0, [150]),
    (1, [100])
])
def test_delete_by_index(some_linked_list, index, expected_list):
    """
    Check method test delete by index. Use parametrize.
    """
    some_linked_list.delete(index)
    assert list(some_linked_list) == expected_list
