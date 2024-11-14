#!/usr/bin/python3
"""
This module defines the Student class with attributes and a method
to retrieve its dictionary representation for JSON serialization,
with an optional filter on specific attributes.
"""


class Student:
    """
    Represents a student with first name, last name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age.
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If `attrs` is a list of strings, only those attributes in the list
        are included in the result. Otherwise, all attributes are included.
        Args:
            attrs (list): A list of attribute names to retrieve.
        Returns:
            dict: A dictionary of the instance's attributes.
        """
        if isinstance(attr, list) and all(isinstance(attr, str) for attr in attr):
            return {attr: getattr(self, attr) for attr in attr if hasattr(self, attr)}
        return self.__dict__