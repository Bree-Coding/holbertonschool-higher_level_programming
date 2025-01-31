#!/usr/bin/python3

"""class that define a square with a public instance method: def area(self),
a private instance attribute: size and Private instance attribute: position"""


class Square:

    """__init__ initializes the size of the square
        size = 0, which referses to the size of the square
        position is a tuple and the position of the square
        value is the new size of the square
        size must be an integer, otherwise TypeError
        size must be >= 0, otherwise ValueError"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for num in value:
            if num is not int or num < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    """Return the current square area"""
    def area(self):
        return self.__size ** 2

    """Prints the square with the character '#'
    If the size is 0, it prints an empty line"""
    def my_print(self):
        if self.__size > 0:
            for x in range(self.__position[1]):
                print()
            for y in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
