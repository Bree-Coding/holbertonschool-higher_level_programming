#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer using "{:d}".format().
    value can be any type.
    Returns True if value is an integer and has been correctly printed.
    Otherwise, returns False."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
