#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_positive_numbers(self):
        """Test list of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -1]), -1)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-100, 50, 0, 25, -75]), 50)

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-7]), -7)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicates(self):
        """Test list with duplicate maximum values"""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_unsorted_list(self):
        """Test unsorted lists"""
        self.assertEqual(max_integer([10, 1, 9, 2]), 10)
        self.assertEqual(max_integer([1, 2, 9, 3, 9]), 9)

    def test_invalid_inputs(self):
        """Test invalid inputs"""
        with self.assertRaises(TypeError):
            max_integer("string")
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()