#!/usr/bin/python3
from rectangle import Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square's sides. Must be a positive
                        integer, validated by integer_validator.
        """
        self.integer_validator("size", size)  # Validate size using parent method
        self.__size = size  # Private size attribute

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the square description as [Square] <width>/<height>.

        Returns:
            str: The string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"