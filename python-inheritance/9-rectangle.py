#!/usr/bin/python3

"""Module that defines a Rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("heighr", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the square.

        Returns:
            str: The string representation of the square.
        """
        return ("[rectangle] {}/{}".format(self.__width, self.__height))
