"""This mod contains class Node for basic structures"""


class BasicNode:
    """
    Node for base structures
    """

    def __init__(self, data, link=None):
        self._data = data
        self._link = link

    @property
    def link(self):
        """
        Create property which get link.
        """
        return self._link

    @property
    def data(self):
        """
        Create property which get value.
        """
        return self._data

    @link.setter
    def link(self, data):
        """
        Create setter which  set new link.
        """
        self._link = data

    @data.setter
    def data(self, data):
        """
        Create setter set new data.
        """
        self._data = data

    def __str__(self):
        return f'[Value={self.data}, Link={self.link}]'
