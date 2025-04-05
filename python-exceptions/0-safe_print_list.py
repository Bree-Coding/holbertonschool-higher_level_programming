#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.
    my_list is the list to print.
    x is the number of elements.
    Returns the number of elements printed."""
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
