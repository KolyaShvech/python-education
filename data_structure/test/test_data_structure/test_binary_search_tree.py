"""
Module testing class BinarySearchTree.
"""

import copy

from data_structure.data_structure.bin_tree_node import TreeNode
from data_structure.data_structure.binary_search_tree import BinarySearchTree


def test_check_branch_to_data():
    """
    Check test func method test_check_branch_to_data.
    """
    test_branch = BinarySearchTree(6)
    assert test_branch._check_branch_to_data(test_branch.head, True) is True
    assert test_branch._check_branch_to_data(test_branch.head, False) is True
    # then add two different element to left and right branches
    test_branch.insert(3)
    test_branch.insert(10)
    # check func when test branch have two branches
    assert test_branch._check_branch_to_data(test_branch.head, True) is False
    assert test_branch._check_branch_to_data(test_branch.head, False) is False


def test_select_branch():
    """
    Check test method about get next move on branches (if move to right, this is True).
    """
    test_branch = BinarySearchTree(11)
    assert test_branch._select_branch(test_branch.head, 20) is True
    assert test_branch._select_branch(test_branch.head, 10) is False


def test_insert_to_empty_tree():
    """
    Check test method test_insert_to_empty_tree, if we insert value to empty tree.
    """
    test_tree = BinarySearchTree(20)
    test_tree.delete_data(20)
    # insert next value
    node_to_insert = BinarySearchTree(15)
    test_tree._insert_to_empty_tree(node_to_insert)
    assert test_tree.count == 1 and test_tree.head == node_to_insert


def test_insert_if_node_none():
    """
    Check test helper method about insert if node none.
    """
    default_tree = BinarySearchTree(8)
    default_tree.delete_data(8)
    element = 8
    previous_node = TreeNode(3)
    node_to_insert = TreeNode(1)
    default_tree._insert_if_node_none(previous_node, node_to_insert, element)
    assert previous_node.right == node_to_insert


def test_insert_to_tree():
    """
    Check test method test_insert_to_tree about insert value to middle position in  tree.
    """
    tree_bst = BinarySearchTree(8)
    node = TreeNode(12)
    node_to_insert = TreeNode(25)
    tree_bst._insert_to_tree(True, True, node, node_to_insert)
    assert node.right == node_to_insert and tree_bst.count == 2


def test_insert():
    """
    Check test method test_insert about insert data to tree.
    """
    tree_bst = BinarySearchTree(10)
    tree_bst.insert(5)
    assert str(tree_bst.head.left) == str(TreeNode(5))
    tree_bst.insert(99)
    assert str(tree_bst.head.right) == str(TreeNode(99))


def test_lookup():
    """
    Check method test_lookup about get element(branch) by data.
    """
    tree_bst = BinarySearchTree(30)
    tree_bst.insert(13)
    tree_bst.insert(18)
    tree_check = copy.deepcopy(tree_bst)  # create deepcopy for check and check delete func too
    tree_check.delete_data(30)
    assert str(tree_bst.look_up(13).right) == str(TreeNode(18))


def test_check_and_delete_head():
    """
    Check test method test_check_and_delete_head about deleting once element - head.
    """
    tree_one_element = BinarySearchTree(30)
    assert tree_one_element._check_and_delete_head(12) is False
    assert tree_one_element._check_and_delete_head(30) is True
    assert tree_one_element.count == 0


def test_check_empty_tree():
    """
    Check test method test_check_empty_tree about empty tree.
    """
    tree_delete = BinarySearchTree(87)
    assert tree_delete._check_tree_empty() is False
    tree_delete.delete_data(87)
    assert tree_delete._check_tree_empty() is True


def test_support_to_delete_branch():
    """
    Check test helper method test_support_to_delete_branch about deleting data in tree.
    """
    tree_bst = BinarySearchTree(126)
    tree_bst._position_branch = True
    tree_bst._former_branch = BinarySearchTree(70)
    tree_bst._former_branch.right = tree_bst
    tree_bst._support_to_delete_branch(11)
    assert tree_bst._former_branch.right == 11


def test_delete_branch_without_children():
    """
    Check test method test_delete_branch_without_children about deleting branch if he
    hasn't children.
    """
    tree_bst = BinarySearchTree(41)
    tree_bst.insert(70)
    tree_bst._delete_branch_without_children(tree_bst.head.right)
    assert tree_bst.count == 1 and tree_bst.head.right is None


def test_delete_branch_with_left_children():
    """
    Check test method test_delete_branch_with_left_children. About delete branch in situation
    when element have left children.
    """
    tree_bst = BinarySearchTree(41)
    tree_bst.insert(68)
    tree_bst.insert(48)
    branch_to_delete = TreeNode(68)
    branch_to_delete.left = TreeNode(48)
    tree_bst._del_branch_with_left_child(branch_to_delete)
    assert str(tree_bst.head.right) == str(branch_to_delete)


def test_delete_branch_with_right_children():
    """
    Check test methodtest_delete_branch_with_right_children. About delete branch in
    situation when element have right children.
    """
    tree_bst = BinarySearchTree(21)
    tree_bst.insert(68)
    tree_bst.insert(123)
    branch_to_delete = TreeNode(68)
    branch_to_delete.right = TreeNode(123)
    tree_bst._del_branch_with_left_child(branch_to_delete)
    assert str(tree_bst.head.right) == str(branch_to_delete)


def test_delete_branch_with_two_children():
    """
    Check test method test_delete_branch_with_two_children, if deleting element have two children.
    """
    tree_bst = BinarySearchTree(5)
    tree_bst.insert(100)
    tree_bst.insert(10)
    tree_bst.insert(150)
    right_branch = TreeNode(10)
    right_branch.right = TreeNode(150)
    tree_bst._del_branch_with_two_child(tree_bst.head.right)
    assert str(tree_bst.head.left) == str(right_branch)


def test_delete_data():
    """
    Check test method test_delete_data about delete selected element.
    """
    tree_bst = BinarySearchTree(100)
    tree_bst.insert(25)
    tree_bst.insert(500)
    tree_bst.insert(321)
    tree_bst.delete_data(500)
    test_branch = TreeNode(100)
    test_branch.left = TreeNode(25)
    test_branch.right = TreeNode(321)
    assert str(tree_bst.head) == str(test_branch)

