#!/usr/bin/python3

"""
This module provides a function to return the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of attributes and methods of an object"""
    return dir(obj)
