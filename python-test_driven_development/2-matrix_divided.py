#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix elements are not lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimals.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                         "integers/floats")

    if not all(all(isinstance(ele, (int, float)) for ele in row) for row
               in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                         "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]