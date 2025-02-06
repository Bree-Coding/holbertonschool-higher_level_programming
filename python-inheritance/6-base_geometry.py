#!/usr/bin/python3

"""Module that defines a base geometry class."""

class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raises an exception indicating that the area method
        is not implemented.
        """
        raise Exception("area() is not implemented")
