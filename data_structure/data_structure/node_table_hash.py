"""
This module contains Node for HashTable.
"""
from data_structure.data_structure.basic_node import BasicNode


class NodeTable(BasicNode):
    """
    Create class Nodetable with parameters value, hash_value, hash_link.
    """

    def __init__(self, value, hash_value, hash_link=None):
        super().__init__(value)
        self._hash_value = hash_value
        self._hash_link = hash_link

    @property
    def hash_value(self):
        """
        Create property hash_value. Get hash value.
        """
        return self._hash_value

    @hash_value.setter
    def hash_value(self, value):
        """
        Create setter hash_value. Set new value to hash.
        """
        self._hash_value = value

    @property
    def hash_link(self):
        """
        Create property hash_link. Get hash link.
        """
        return self._hash_link

    @hash_link.setter
    def hash_link(self, value):
        """
        Create setter hash_link. Set new link to hash.
        """
        self._hash_link = value

    def __str__(self):
        return f'[Value={self.data}, Hash={self.hash_value}, HashLink={self.hash_link}, Link={self.link}]'
