"""
In this module is a class TreeNode for class BinarySearchTree.
"""


class TreeNode:
    """
    Create TreeNode for Binary Search Tree.
    """

    def __init__(self, data):
        self._left = None
        self._data = data
        self._right = None

    @property
    def left(self):
        """
        Create property left for get left child.
        """
        return self._left

    @property
    def right(self):
        """
        Create property right for get right child.
        """
        return self._right

    @property
    def data(self):
        """
        Create property data for get value.
        """
        return self._data

    @left.setter
    def left(self, value):
        """
        Create setter left for set value to left child.
        """
        self._left = value

    @right.setter
    def right(self, value):
        """
        Create setter left for set value to left child.
        """
        self._right = value

    @data.setter
    def data(self, value):
        """
        Create setter date for set new value.
        """
        self._data = value

    def __str__(self):
        return f'[Value={self.data}, Left={self.left}, Right={self.right}]'
