#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student():
    """
    Initializes a new Student instance.

    Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age
    """
    Retrieves a dictionary representation of a Student instance.
    """
    def to_json(self):
        """
          Returns a dictionary representation of the Student instance.
        """
        return obj.__dict__
