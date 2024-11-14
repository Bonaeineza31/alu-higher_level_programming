#!/usr/bin/python3
"""
This module defines the pascal_triangle function that generates
Pascal's Triangle of a given size.
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to n rows.
    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of lists: A list of lists where ea in Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
