#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number (div).

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Returns:
     list:matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
     raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
     raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
     raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
     raise TypeError("div must be a number")
    if div == 0:
     raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]