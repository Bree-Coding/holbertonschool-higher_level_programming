#!/usr/bin/python3

"""This module defines a class Rectangle that represents a rectangle.
    width is width of the rectangle
    height height of the rectangle"""


class Rectangle:
    """Initialization of the class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """area returns the area of the rectangle"""
    def area(self):
        return self.__width * self.__height

    """perimeter returns the perimeter of the rectangle"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2 + self.__height * 2)

    """str is the representation of the rectangle made with #,
        or an empty string"""
    def __str__(self):
        rect = ""
        if self.__width > 0 and self.__height > 0:
            for x in range(self.__height):
                rect += str(self.print_symbol) * self.__width + "\n"
            return rect[:-1]
        if self.__width == 0 or self.__height == 0:
            return ""

    """Returns a string that represents the rectangle for
    debugging and development purposes."""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    """Prints a message when an instance of Rectangle is deleted"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
