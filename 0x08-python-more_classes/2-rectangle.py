#!/usr/bin/python3
"""This module computes the area and perimeter of a Rectangle"""


class Rectangle:
    """This creates an instance of Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the instance by calling the setter methods"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if (self.__height == 0 or self.__width == 0):
            return 0
        return (2*self.__height) + (2*self.__width)
