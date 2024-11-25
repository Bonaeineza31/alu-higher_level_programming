#!/usr/bin/python3
"""
This module provides a function to print a square using the character '#'.
"""

def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size of the square (length of its sides).

    Raises:
        TypeError: If size is not an integer or is a float < 0.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(1)
        #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)