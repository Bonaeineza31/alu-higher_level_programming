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
    
    result = ""
    for char in text:
        result += char
        if char in ".:?":
            result += "\n\n"
    # Remove leading/trailing spaces from each line
    result = "\n".join([line.strip() for line in result.split("\n")])
    print(result)