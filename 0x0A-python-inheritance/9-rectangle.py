#!/usr/bin/python3
"""This module contains Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle  inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes and validates protected attributes"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """implements area"""
        return self.__width * self.__height

    def __str__(self):
        """return string in print()"""
        return f"[Rectangle] {self.__width}/{self.__height}"
