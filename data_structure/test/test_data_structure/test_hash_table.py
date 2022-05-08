"""Testing class HashTable"""
import copy

import pytest

from data_structure.data_structure.hash_table import HashTable


def test_get_hash():
    """
    Check test about get real hash data.
    """
    test_table = HashTable('nemo')
    assert test_table._get_hash('kolya') == 4
    assert test_table.head.hash_value == 11


def test_insert():
    """Check testing about insert data to hash table.
    """
    test_table = HashTable('kolya')
    test_table.insert('kolya')
    assert test_table.head.hash_value is not None
    assert str(test_table.head.hash_link) == str(HashTable('kolya').head)


def test_delete_other():
    """
    Check test about deleting element in big table and check collision.
    """
    test_table = HashTable('kolya')
    test_table.insert('nemo')
    test_table.delete(11)
    assert test_table.count == 1 and test_table.head.link is None


def test_delete_first():
    """Check test about delete first element in hash table.
    """
    test_table = HashTable('kolya')
    test_table._delete_first()
    assert test_table.count == 0 and test_table.head is None


def test_delete():
    """
    Check test main func about delete element from table by hash.
    """
    test_table = HashTable('kolya')
    test_table.insert('nemo')
    test_table.delete(4)
    assert test_table.head.data == 'nemo' and test_table.count == 1
    test_table.delete(11)
    assert test_table.count == 0 and test_table.head is None


def test_check_collision():
    """Check test func about check collision.
    """
    test_table = HashTable('kolya')
    assert test_table._check_collision(test_table.head) is False
    test_table.insert('kolya')
    assert test_table._check_collision(test_table.head) is True


@pytest.mark.parametrize('nodes', [(HashTable('kolya').head, HashTable('nemo').head)])
def test_check_tail(nodes):
    """Check test test_check_tail, helper method about deleting last element.
    """
    test_table = HashTable('kolya')
    test_table._check_next_tail(*nodes)
    assert test_table.tail.hash_value == nodes[0].hash_data


def test_look_up():
    """Check test method about look_up data by hash.
    """
    test_table = HashTable('mitya')
    test_table.insert('kolya')
    test_table.insert('kolya')
    check = copy.deepcopy(test_table)
    assert test_table.look_up(8) == check.head.data
    assert test_table.look_up(4) == check.head.link.data
