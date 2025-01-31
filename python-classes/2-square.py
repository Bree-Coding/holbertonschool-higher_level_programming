#!/usr/bin/python3

"""class that define a square with a private instance attribute: size"""


class Square:

    """__init__ initializes the size of the square
        size = 0, which referses to the size of the square
        size must be an integer, otherwise TypeError
        size must be >= 0, otherwise ValueError"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
