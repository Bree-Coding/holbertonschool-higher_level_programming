#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    min_int = min(my_list)
    for x in my_list:
        if x > min_int:
            min_int = x
    return min_int
