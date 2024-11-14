#!/usr/bin/python3
"""
This module provides a function to load a Python object from a JSON file.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: An instance of a Class.
    Returns:
        dict: A dictionary representation of obj.
    """
    return obj.__dict__
