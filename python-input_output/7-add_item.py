#!/usr/bin/python3
import sys
"""
Import functions to save and load JSON objects
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""
Try to load the existing list from the JSON file
"""



try:
    lst = load_from_json_file("add_item.json")
    """
    If the file does not exist, initialize an empty list
    """
except FileNotFoundError:
    lst = []
"""
Add each command line argument to the list
"""
for x in range(1, len(sys.argv)):
    lst.append(sys.argv[x])
"""
Save the updated list to the JSON file
"""
save_to_json_file(lst, "add_item.json")
