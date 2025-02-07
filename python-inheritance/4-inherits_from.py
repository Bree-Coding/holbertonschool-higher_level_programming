#!/usr/bin/python3

"""Module that defines a function to check if an object
is an instance of a class
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class

    Returns:
        True if obj is an instance inherited; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
