"""
Module test quick sort.
"""
import unittest

from algorithms_code.interactive_qiuck_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    """
    Create class TestQuickSort.
    """
    def test_quick_sort(self):
        """
        Check quick sort with integer.
        """
        array = [6, 7, 4, 1, 2, 3, 9, 10, 2]
        expected = [1, 2, 2, 3, 4, 6, 7, 9, 10]
        self.assertEqual(quick_sort(array), expected)

    def test_quick_sort_str(self):
        """
        Check quick sort with string.
        """
        data = ['ty', 'rtr', 'op', 'qw', 'cv']
        expected = ['cv', 'op', 'qw', 'rtr', 'ty']
        self.assertEqual(quick_sort(data), expected)
