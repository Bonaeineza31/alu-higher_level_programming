#!/usr/bin/python3
"""
This module defines a Square class with size and position, validation for size,
methods to search it's area, and  method to print it using the character "#",.
"""


class Square:
    """
    Represents a square with valid size,position and methods to print the square.
    Attributes:
        __size (int):size of a side of the square. Must be an integer and >= 0.
        __position (tuple):2 positive integers representing the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with a given size and position.
        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple,): it's position is given by a tuple of two integers.
        Raises:
            TypeError: If size isn't integer/position then it's tuple of 2 + integers.
            ValueError: If size is less than 0 or position integers are not +.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the position of the square.
        Returns:
            tuple: The position of the square as a tuple of two integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.
        Args:
            value (tuple): Should be a tuple of two positive integers.
        Raises:
            TypeError: If the value is not a tuple of two + integers.
            ValueError: If the values are not positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value) or not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character "#" with spaces for position.
        If the size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            # Print the vertical offset (position[1] spaces)
            for _ in range(self.__position[1]):
                print()
            # Print the square with horizontal offset (position[0] spaces)
            for _ in range(self.__size):
             print(" " * self.__position[0] + "#" * self.__size)