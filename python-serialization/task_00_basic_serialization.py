#!/usr/bin/env python3
"""
This module provides functions to serialize data to a file and deserialize
data from a file using the pickle module.
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    Serialize the given data and save it to the specified file.
    """

    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from the specified file.
    """

    with open(filename, 'rb') as file:
        return pickle.load(file)
