#!/usr/bin/python3
"""
The  module defines a class `MyList` that inherit4rm the built-in `list` 
class. The class has a public instance method `print_sorted` that prints
the list in ascending order.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list class and includes a
    method to print the list in sorted order.
    """
    
    def print_sorted(self):
        """
        Prints the list sorted in ascending order without modifying the original
        list.
        """
        print(sorted(self))
