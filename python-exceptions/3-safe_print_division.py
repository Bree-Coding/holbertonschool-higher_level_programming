#!/usr/bin/python3

def safe_print_division(a, b):
    """Divides 2 integers and prints the result.
    a and b are integers.
    Returns the result of the division, otherwise None."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
