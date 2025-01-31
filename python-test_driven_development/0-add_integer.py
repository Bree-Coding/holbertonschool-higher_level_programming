#!/usr/bin/python3

def add_integer(a, b=98):

    """This function adds two integers or floats and return the result.
    An error message is desplay if a or b is not an integer or a float.
    a is the first integer or float to be added.
    b is the second integer or float to be added."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
