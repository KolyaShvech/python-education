"""
Module test binary search.
"""
import unittest

from algorithms_code.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """
    Create class TestBinarySearch.
    """
    def test_binary_search(self):
        """
        Check binary search.
        """
        self.assertEqual(binary_search([4, 6, 2, 1], 3), -1)
        self.assertEqual(binary_search([10, 20, 30, 40, 50], 8), -1)
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(binary_search([5, 6, 10, 8], 6), 1)
