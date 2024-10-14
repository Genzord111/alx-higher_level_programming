#!/usr/bin/python3
"""This module contains an empty class"""


class BaseGeometry:
    """This class for calculating area"""

    def area(self):
        """raises an exception if no area is calculated"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is positive non-zero integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

