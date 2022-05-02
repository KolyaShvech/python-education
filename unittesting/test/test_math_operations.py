"""
Testing code with math operations.
"""

import unittest
from unittesting.unittesting.math_operations import even_odd, sum_all

class TestOdd(unittest.TestCase):
    """
    Create class TestOdd unittest.TestCase.
    """

    def test_even(self):
        """
        Check even numbers in different various.
        """
        self.assertEqual(even_odd(10), 'even')
        self.assertEqual(even_odd(0), 'even')
        self.assertEqual(even_odd(-2), 'even')

    def test_odd(self):
        """
        Check odd numbers in different various.
        """
        self.assertEqual(even_odd(7), 'odd')
        self.assertEqual(even_odd(-9), 'odd')

    def test_string(self):
        """
        Raise error string, TypeError.
        """
        self.assertRaises(TypeError, even_odd, str)

    def test_float(self):
        """
        Raise flout numbers, TypeError.
        """
        self.assertRaises(TypeError, even_odd, float)


class TestSumAll(unittest.TestCase):

    def test_sum_all_positive_numbers(self):
        """
        Check sum_all with positive numbers.
        """
        self.assertEqual(sum_all(2, 3, 4), 9)

    def test_sum_all_negative_numbers(self):
        """
        Check sum_all with negative numbers.
        """
        self.assertEqual(sum_all(-1, -4, -7), -12)

    def test_sum_all_different_numbers(self):
        """
        Check sum_all with different numbers.
        """
        self.assertEqual(sum_all(6, -3, 11, -2), 12)

    def test_sum_all_positive_float_numbers(self):
        """
        Check sum_all with float numbers.
        """
        self.assertEqual(sum_all(7.4, 2.1, 10.3), 19.8)

    def test_sum_all_negative_float_numbers(self):
        """
        Check sum_all with negative float numbers.
        """
        self.assertEqual(sum_all(-4.2, -1.7, -9.6), -15.5)

    def test_sum_all_different_float_numbers(self):
        """
        Check sum_all with different float numbers.
        """
        self.assertEqual(sum_all(9.7, -7.6, 17.9, -7.3), 12.7)

    def test_sum_all_wrong_input_str(self):
        """
        Raise error TypeError type(str).
        """
        self.assertRaises(TypeError, sum_all, str)

    def test_sum_all_type_list(self):
        """
        Raise error TypeError type(list).
        """
        self.assertRaises(TypeError, sum_all, list)

    def test_sum_all_type_tuple(self):
        """
        Raise error TypeError type(tuple).
        """
        self.assertRaises(TypeError, sum_all, tuple)

    def test_sum_all_type_dict(self):
        """
        Raise error TypeError type(dict).
        """
        self.assertRaises(TypeError, sum_all, dict)

    def test_sum_all_type_set(self):
        """
        Raise error TypeError type(set).
        """
        self.assertRaises(TypeError, sum_all, set)

if __name__ == "__main__":
    unittest.main

