#!/usr/bin/python3
"""
This module provides a CustomObject class with methods
to serialize and deserialize instances using the pickle module.
"""
import pickle


class CustomObject:
    """
    A class to represent a custom object with attributes name, age,
    and is_student.
    """
    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject with the specified attributes.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is_student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the given data and save it to the specified file.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and deserialize data from the specified file.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
