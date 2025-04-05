#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers.
    my_list can contain any type of element.
    x is the number of elements in my_list.
    Returns the real number of integers printed."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print()  # Print a new line after the loop
    return count
