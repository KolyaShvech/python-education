"""This mod contains class Graph"""
from data_structure.linked_list import LinkedList
from data_structure.node_graph import NodeGraph


class Graph:
    """
    Create class Graph with parameters: node, head, tail, count and _former.
    """

    count = 0

    def __init__(self, data):
        node = NodeGraph(data)
        self.head = node
        self.tail = node
        self.count += 1
        self._former = None  # property for deleting some element

    def insert(self, data, *args):
        """
        Add element with data and with links about others elements.
        """
        if self.look_up(data) is not None:  # if you have already this data
            return None

        node_to_insert = NodeGraph(data)  # just a insert node.
        self.tail.link = node_to_insert
        self.tail = node_to_insert
        self.count += 1

        len_args = len(args)  # operate from any connection
        index = 0
        node = self.head
        while index != self.count:
            if node is None:
                break
            index_args = 0
            while index_args != len_args:
                if node.data == node_to_insert.data:
                    for char in args:
                        self._add_connections(node, char)
                    index_args += 1
                    break

                if node.data == args[index_args]:
                    self._add_connections(node, node_to_insert.data)  # add connections
                index_args += 1
            index += 1
            node = node.link

    @staticmethod
    def _add_connections(node: NodeGraph, value_to_insert):
        if node.connections is None:
            node.connections = LinkedList(value_to_insert)
        else:
            node.connections.append(value_to_insert)

    def look_up(self, data):
        """
        Search node by data and return link for this node.
        """
        node = self.head
        index = 0
        while index != self.count:
            if node.data == data:
                return node
            index += 1
            node = node.link
        return None

    def _delete_only_element(self, data):
        """
        Delete only element. Protected method.
        """
        if self.count == 1 and self.head.data == data:
            self.head = None
            self.count -= 1
            return True
        return False

    def _delete_just_element(self, data):
        """
        Protected method for delete just element.
        """
        node = self.head
        index = 0
        while index != self.count:
            if node.data == data:
                if node.link is None:
                    self._former.link = None
                    self.count -= 1
                    break
                self._former.link = node.link
                self.count -= 1
                break
            index += 1
            self._former = node
            node = node.link

    def _delete_all_connections(self, deleted_data):
        """
        Protected method for delete all connections.
        """
        node = self.head
        index = 0
        while index != self.count:  # delete connections by func delete in custom LinkedList
            index = node.connections.look_up(deleted_data)  # search deleting index
            node.connections.delete(index)  # deleting connect by index
            index += 1
            node = node.link

    def delete(self, data):
        """
        Delete node by value and other nodes with this node.
        """
        if self._delete_only_element(data):  # if graph have only element
            return None
        if self.look_up(data) is None:  # if deleting element not in graph
            return None
        self._delete_just_element(data)  # firstly we need delete element and then - connections
        self._delete_all_connections(data)  # and then - deleting all connections
        return None
