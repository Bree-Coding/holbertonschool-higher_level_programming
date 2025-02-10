#!/usr/bin/python3
"""
ted: 0.00%)
Write a function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Returns the dictionary description for JSON serialization
    of an object.
    """
    return obj.__dict__
