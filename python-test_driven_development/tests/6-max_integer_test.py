#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_positive_integers(self):
        """Test with a list of positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, 5, 20, 15]), 20)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -50, -20, -15]), -10)

    def test_mixed_integers(self):
        """Test with a mix of positive and negative integers."""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-10, 50, 20, -15]), 50)

    def test_single_element(self):
        """Test with a single element in the list."""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.8, 3.6, 4.1]), 4.1)
        self.assertEqual(max_integer([-1.5, -2.8, -3.6, -0.1]), -0.1)

    def test_mixed_numbers(self):
        """Test with a mix of integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, 4.8]), 4.8)
        self.assertEqual(max_integer([-1, -2.5, -3, -0.8]), -0.8)

    def test_duplicates(self):
        """Test with duplicate values in the list."""
        self.assertEqual(max_integer([2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_strings(self):
        """Test with strings."""
        self.assertEqual(max_integer(["a", "b", "c", "z"]), "z")
        self.assertEqual(max_integer(["ant", "boy", "car"]), "cherry")

    def test_invalid_input(self):
        """Test with invalid input."""
        with self.assertRaises(TypeError):
            max_integer(123)
        with self.assertRaises(TypeError):
            max_integer(["a", 2, 3])


if __name__ == "__main__":
    unittest.main()