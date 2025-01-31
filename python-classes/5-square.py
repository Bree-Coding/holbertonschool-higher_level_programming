#!/usr/bin/python3

"""class that define a square with a public instance method: def area(self),
a private instance attribute: size and Private instance attribute: position"""


class Square:

    """__init__ initializes the size of the square
        size = 0, which referses to the size of the square
        value is the new size of the square.
        size must be an integer, otherwise TypeError
        size must be >= 0, otherwise ValueError"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    """Return the current squarearea"""
    def area(self):
        return self.__size ** 2

    """Prints the square with the character '#'. If the size is 0, it prints an empty line."""
    def my_print(self):
        if self.__size > 0:
            for x in range(self.__size):
                print("#" * self.__size)
        else:
            print()
