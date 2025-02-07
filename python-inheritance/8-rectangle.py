#!/usr/bin/python3

"""Module that defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("heighr", height)
        self.__width = width
        self.__height = height
