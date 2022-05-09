"""
This module consist class HashTable.
"""
from data_structure.data_structure.node_table_hash import NodeTable


class HashTable:
    """
    Create class HashTable and implements his methods.
    """

    count = 0
    hash_standard_len = 30

    def __init__(self, data):
        node = NodeTable(data, self._get_hash(data))
        self.head = node
        self.tail = node
        self.count += 1

    def _get_hash(self, data):
        """
        Create protected method hash for current data.
        """
        summary = 0
        for char in data:
            summary += ord(char)
        return summary % self.hash_standard_len

    def insert(self, data):
        """
        Create method insert current data to current hash table.
        """
        hash_data = self._get_hash(data)
        node_to_insert = NodeTable(data, hash_data)
        index = 0
        node = self.head
        while index != self.count:
            if node is None:
                break
            if node.hash_value == hash_data:
                node.hash_link = node_to_insert
                self.count += 1
                return None
            index += 1
            node = node.link

        self.tail.link = node_to_insert
        self.tail = node_to_insert
        self.count += 1

    def _delete_other(self, hash_data):
        """
        Create protected method _delete_other.Method element by hash data and check can it be
        collision.
        """
        node = self.head
        node_previous = None
        counter = 0
        while counter != self.count:
            if node is None:
                break
            if node.hash_value == hash_data:
                if self._check_collision(node):  # check collision.
                    node.hash_link = None
                else:
                    node_to_delete = node_previous.link
                    self._check_next_tail(node_previous, node_to_delete)
                    node_previous.link = node_to_delete.link
                    break
            counter += 1
            node_previous = node
            node = node.link
        self.count -= 1

    def _delete_first(self):
        """
        Create protected method _delete_first. If by hash data is a first_element.
        """
        if self.head.hash_link is None:
            self.head = self.head.link
        else:
            self.head.hash_link = None
        self.count -= 1

    def delete(self, hash_data):
        """
        Create method delete. Method delete data by hash data.
        """
        if hash_data == self.head.hash_value:
            self._delete_first()
        else:
            self._delete_other(hash_data)

    @staticmethod
    def _check_collision(node: NodeTable):
        """
        Protected staticmethod _check_collision. Method check collision if data insert to hash table.
        """
        if node.hash_link is not None:
            return True
        return False

    def _check_next_tail(self, node_now: NodeTable, node_next: NodeTable):
        """
        Create protected method _check_next_tail. Method delete element if is a tail.
        """
        if node_next is self.tail:
            self.tail = node_now

    def look_up(self, hash_data):
        """
        Create method look_up. Method get data by hash to look.
        """
        node = self.head
        index = 0
        while index != self.count:
            if node.hash_value == hash_data:
                return node.data
            index += 1
            node = node.link
        return None

