#!/usr/bin/python3
"""
Module for adding text indentation after specific characters.
"""


def text_indentation(text):
    """Prints text with two new lines after `.`, `:`, and `?`.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Initialize result string
    result = ""
    # Flag to manage leading spaces
    skip_space = True
    
    for char in text:
        if char in ".:?":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False

    print(result.strip())