#!/usr/bin/python3
"""Module contains square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from Rectangle class"""

    def __init__(self, size):
        """Instantiation with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Implementation of area"""
        return self.__size**2
