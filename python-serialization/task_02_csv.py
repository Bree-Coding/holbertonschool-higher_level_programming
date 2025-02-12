#!/usr/bin/python3
"""
This module provides a function to convert a CSV file to a JSON file.
"""

import csv 
import json


def convert_csv_to_json(csv_filename):
    """
    Convert the given CSV file to a JSON file named data.json.
    """
    try:
        with open(csv_filename, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
            
        with open('data.json', mode='w') as file:
            json.dump(data, file)
        return True

    except FileNotFoundError:
        return False

    except Exception:
        return False
