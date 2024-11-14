#!/usr/bin/python3
"""
This module provides function to save Python object to file in JSON format.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file using JSON representation.

    Args:
        my_obj (object): The object to be saved to the file.
        filename (str): The name of the file to save the JSON data to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
