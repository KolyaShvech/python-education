"""Module testing class Graph"""


from data_structure.data_structure.graph import Graph
from data_structure.data_structure.linked_list import LinkedList
from data_structure.data_structure.node_graph import NodeGraph


def test_insert():
    """
    Check test func about insert to graph.
    """
    graph = Graph(5)
    graph.insert(3, 5)
    graph.insert(10, 3, 5)
    test_connections = LinkedList(3)
    test_connections.append(10)
    assert str(graph.head.connections.head) == str(test_connections.head)


def test_add_connections():
    """
    Check test func about add connections to element.
    """
    graph = Graph(5)
    node = NodeGraph(3)
    graph._add_connections(node, 5)
    to_test = LinkedList(5)
    assert str(node.connections.head) == str(to_test.head)


def test_look_up():
    """
    Check test func about get link for node by data.
    """
    graph = Graph(10)
    graph.insert(15, 10)
    graph.insert(25, 10, 15)
    assert graph.look_up(10).connections.head.data == 15
    to_test_list = LinkedList(15)
    to_test_list.append(25)
    assert str(graph.head.connections.head) == str(to_test_list.head)


def test_delete_only_element():
    """
    Check test func about deleting if in graph one element.
    """
    graph = Graph(5)
    # wrong value
    assert graph._delete_only_element(10) is False
    assert graph._delete_only_element(5) and graph.count == 0


def test_delete_just_element():
    """
    Check test func about delete element without connections.
    """
    graph = Graph(5)
    graph.insert(3, 5)
    graph._delete_just_element(3)
    assert graph.head.link is None


def test_delete_all_connections():
    """
    Check test method about delete connections after delete element.
    """
    graph = Graph(5)
    graph.insert(3, 5)
    graph._delete_all_connections(5)
    assert graph.head.connections is None


def test_delete():
    """
    Check test delete.
    """
    graph = Graph(10)
    graph.insert(5, 10)
    graph.delete(5)
    assert graph.count == 1 and graph.head.connections.head is None
