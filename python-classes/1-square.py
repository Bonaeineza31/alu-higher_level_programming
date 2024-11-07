#!/usr/bin/python3

"""
This module defines a Square class.
The class has a private instance attribute 'size' which represents the size of the square.
"""

class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a square with a given size.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size
