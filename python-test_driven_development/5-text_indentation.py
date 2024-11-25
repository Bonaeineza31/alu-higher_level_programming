#!/usr/bin/python3
"""
This module provides fx to format text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.'.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Hello. How are you? I am fine:")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        I am fine:
        <BLANKLINE>
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    result = ""
    temp = text

    for char in chars:
        temp = temp.replace(char, f"{char}\n\n")

    lines = temp.splitlines()
    for line in lines:
        result += line.strip() + "\n"

    print(result, end="")