#!/usr/bin/python3

def add_integer(a, b=98):
    """Function that add two integers or floats and return the result
    or an error message if a or b is not an integer or a float"""
    if not isinstance(a, (int, float))
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float))
        raise TypeError("b must be an integer")
    return int(a) + int(b)
