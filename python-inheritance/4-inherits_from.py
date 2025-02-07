#!/usr/bin/python3

"""Module that defines a function to check if an object
is an instance of a class that inherited (directly or indirectly)
from the specified class.
"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a class
    that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    Returns:
        True if obj is an instance of a class that inherited
        from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
