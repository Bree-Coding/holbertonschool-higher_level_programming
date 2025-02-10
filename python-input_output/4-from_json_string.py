#!/usr/bin/python3

"""
A function that returns the JSON representation of an object (string)
"""


import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object.
    """
    return json.loads(my_str)
