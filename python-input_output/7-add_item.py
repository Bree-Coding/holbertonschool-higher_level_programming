#!/usr/bin/python3
"""
Import functions to save and load JSON objects
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []

for x in range(1, len(sys.argv)):
    lst.append(sys.argv[x])

save_to_json_file(lst, "add_item.json")
