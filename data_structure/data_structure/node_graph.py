"""
Create module NodeGraph. It contains node for graph.
"""
from data_structure.linked_list import LinkedList
from data_structure.basic_node import BasicNode


class NodeGraph(BasicNode):
    """
    Create class NodeGraph. It is Node for class Graph
    """

    def __init__(self, data, connections: LinkedList = None):
        super().__init__(data)
        self._connections = connections

    @property
    def connections(self):
        """
        Create property connections. Get current nodes
        """
        return self._connections

    @connections.setter
    def connections(self, next_connections):
        """
        Create setter connections. Set next connections.
        """
        self._connections = next_connections

    def __str__(self):
        if self.connections is None:
            return f'[Value={self.data}, Connections={self.connections}, Link={self.link}]'
        return f'[Value={self.data}, Connections={self.connections.head}, Link={self.link}]'
