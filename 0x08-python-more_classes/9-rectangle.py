#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """This creates an instance of Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the instance by calling the setter methods"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle" + 3 * '.')
        Rectangle.number_of_instances -= 1

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

    def print_square(self):
        """Creates a string that represents the rectangle with #"""
        recStr = ""
        if (self.__height == 0 or self.__width == 0):
            return recStr
        for i in range(self.__height):
            recStr += (self.__width * str(self.print_symbol))
            if (i != (self.__height - 1)):
                recStr += "\n"

        return recStr

    def __str__(self):
        """Returns the print_square function"""
        return self.print_square()

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the instance with biggest area else rect_1"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates an istance of a square class"""
        return cls(size, size)
