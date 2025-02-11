#!/usr/bin/env python3
"""
This module provides functions to serialize data to a file and deserialize
data from a file using the pickle module.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to the specified file.
    """

    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
