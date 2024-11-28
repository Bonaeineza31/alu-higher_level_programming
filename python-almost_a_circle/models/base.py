#!/usr/bin/python3
"""
Base class for managing object IDs and JSON serialization.
"""
import json


class Base:
    """
    Base class to manage ID attributes and JSON serialization.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.
        Args:
            id (int): The ID of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            str: A JSON string representation of the list.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string back to a list of dictionaries.
         Args:
            json_string (str): A JSON string
        Returns:
            list: The corresponding list of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
