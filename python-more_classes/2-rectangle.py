#!/usr/bin/python3

"""This module defines a class Rectangle that represents a rectangle.
    width is width of the rectangle
    height height of the rectangle"""


class Rectangle:
    """Initialization of the class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
