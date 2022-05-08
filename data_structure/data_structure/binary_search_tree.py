"""
In this module is implement a class Binary Search Tree
"""
from data_structure.bin_tree_node import TreeNode


class BinarySearchTree:
    """
    Create class BinarySearchTree. This class showing how work a binary search tree.
    """

    count = 0

    def __init__(self, data):
        self.head = TreeNode(data)
        self.count += 1
        self._former_branch = None  # create property for deleting element
        self._position_branch = None

    @staticmethod
    def _check_branch_to_data(current_node: TreeNode, location):
        """
        Create staticmethod _check_branch_to_data. Return True if we can append data to tree.
        """
        if location:
            if current_node.right is None:
                return True
            return False
        if current_node.left is None:
            return True
        return False

    @staticmethod
    def _select_branch(select_node: TreeNode, data):
        """
        Create staticmethod _select_branch. Return True if we can move data to right branch.
        """
        if select_node.data < data:
            return True
        return False

    def _insert_to_empty_tree(self, value):
        """
        Create protected _insert_to_empty_tree. Insert value if tree empty.
        """
        self.head = value
        self.count += 1

    def _insert_if_node_none(self, former_node: TreeNode, node_to_insert: TreeNode, value):
        """
        Create protected method _insert_if_node_none. Helps methods if node is None after while.
        """
        if former_node.data < value:
            former_node.right = node_to_insert
        else:
            former_node.left = node_to_insert
        self.count += 1

    def _insert_to_tree(self, selected_branch, permission,
                        node: TreeNode, node_to_insert: TreeNode):
        """
        Create protected method _insert_to_tree. Insert value if his position in center of tree
        """
        if selected_branch and permission:
            node.right = node_to_insert  # can insert to right branch
            self.count += 1
            return True
        if not selected_branch and permission:
            node.left = node_to_insert  # can insert to left branch
            self.count += 1
            return True
        return False

    def insert(self, value):
        """
        Create method insert. Add value to binary tree.
        """
        node_to_insert = TreeNode(value)
        if self._check_tree_empty():  # if tree is empty
            self._insert_to_empty_tree(node_to_insert)
            return None
        if self.look_up(value) is not None:  # if duplicate
            return None

        node = self.head
        index = 0
        previous_node = None
        while index != self.count:
            if node is None:  # if we added value to last branch
                self._insert_if_node_none(previous_node, node_to_insert, value)
                break
            selected_branch = self._select_branch(node, value)  # if we add element in center tree
            permission_to_insert = self._check_branch_to_data(node, selected_branch)
            if self._insert_to_tree(selected_branch, permission_to_insert, node, node_to_insert):
                break

            index += 1
            previous_node = node
            if selected_branch:
                node = node.right
            else:
                node = node.left

    def look_up(self, data):
        """
        Create method look_up. We get link to data.
        """
        node = self.head
        index = 0
        while index != self.count:
            if node is None:
                return None
            if node.data == data:
                return node
            next_branch = self._select_branch(node, data)
            if next_branch and node.data == data:
                return node
            if node.data == data:
                return node
            index += 1
            self._former_branch = node  # set former branch for delete func
            self._position_branch = next_branch
            node = node.right if next_branch else node.left  # set next node

    def _check_and_delete_head(self, data):
        """
        Create protected method _check_and_delete_head. Delete one item and he is head.
        """
        if self.count == 1 and self.head.data == data:
            self.head = None
            self.count -= 1
            return True
        return False

    def _check_tree_empty(self):
        """
        Create method _check_tree_empty. Сhecks the tree for its emptiness
        """
        if self.count == 0:
            return True
        return False

    def _support_to_delete_branch(self, data_for_node):
        """
        Create protected method _support_to_delete_branch. Delete something branch in any situation.
        """
        if self._position_branch:
            self._former_branch.right = data_for_node
        else:
            self._former_branch.left = data_for_node
        self.count -= 1

    def _delete_branch_without_children(self, node_to_delete: TreeNode):
        """
        Create protected method _delete_branch_without_children. Delete branch when branch haven't children.
        """
        if node_to_delete.left is None and node_to_delete.right is None:
            self._support_to_delete_branch(None)  # delete branch
            return True
        return False

    def _del_branch_with_left_child(self, node_to_delete: TreeNode):
        """
        Create protected method _del_branch_with_left_child. This method delete branch when branch
        have a left child.
        """
        if node_to_delete.left is not None and node_to_delete.right is None:
            self._support_to_delete_branch(node_to_delete.left)  # delete branch
            return True
        return False

    def _del_branch_with_right_child(self, node_to_delete: TreeNode):
        """
        Create protected method _del_branch_with_right_child. This method delete branch when branch
        have a right child.
        """
        if node_to_delete.left is None and node_to_delete.right is not None:
            self._support_to_delete_branch(node_to_delete.right)  # delete branch
            return True
        return False

    def _del_branch_with_two_child(self, node_to_delete: TreeNode):
        """
        Create protected method _del_branch_with_two_child. This method delete branch when branch
        have two children.
        """
        if node_to_delete.left and node_to_delete.right:
            node = node_to_delete.left  # search max item in left branch current node to delete
            index = 0

            node_to_del_position = None  # this node to position after deleting node
            previous_node = None

            node_in_air_left = node_to_delete.left  # link to nodes if long deleting
            node_in_air_right = node_to_delete.right

            while index != self.count:  # get necessary elements
                node_to_del_position = node
                if node.right is None:
                    break
                previous_node = node
                index += 1
                node = node.right

            if self._position_branch:  # proces permutations for delete element with two children
                self._former_branch.right = node_to_del_position
            else:
                self._former_branch.left = node_to_del_position

            node_to_del_position.left = node_in_air_left  # create connections with branches
            node_to_del_position.right = node_in_air_right

            previous_node.right = None  # clear right child after reposition
            self.count -= 1
            return True
        return False

    def delete_data(self, data):
        """
        Create method delete_data. Delete item by data.
        """
        if self._check_and_delete_head(data):  # check to one head and maybe delete this
            return None
        node_to_delete = self.look_up(data)  # get node for delete
        if node_to_delete is not None:  # search situation about current node to delete
            if self._delete_branch_without_children(node_to_delete):
                return None
            if self._del_branch_with_left_child(node_to_delete):
                return None
            if self._del_branch_with_right_child(node_to_delete):
                return None
            if self._del_branch_with_two_child(node_to_delete):
                return None
            return None
