#!/usr/bin/python3
"""
Module for adding text indentation after specific characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Characters that trigger double newlines
    delimiters = {".", "?", ":"}
    result = ""
    i = 0

    while i < len(text):
        char = text[i]
        result += char
        if char in delimiters:
            result += "\n\n"
            # Skip any spaces following the delimiter
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    # Print the formatted text without trailing spaces
    print(result.strip())