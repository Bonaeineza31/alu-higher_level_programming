#!/usr/bin/python3
"""
This module provides a function to append a string to a text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends a string text file returns nbr of characters added."""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
