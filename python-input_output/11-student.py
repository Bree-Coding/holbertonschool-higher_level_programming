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
        self.age = age

    """
    """
    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        resultat = {}
        if type(attrs) is list:
            for element in sorted(attrs):
                if type(element) is not str:
                    return self.__dict__
                else:
                    if element in self.__dict__:
                        resultat[element] = self.__dict__[element]
            return resultat

        return sorted(self.__dict__)

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
