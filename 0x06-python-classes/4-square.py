#!/usr/bin/python3
"""This is the 1-square module"""


class Square:
    """Creates an instance of the class Square"""

    def __init__(self, size=0):
        """Initializes size with a positive integer value"""
        try:
            if (size < 0):
                raise ValueError('size must be >= 0')
            self._Square__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
    
    @property
    def size(self):
        """Function to retrieve size"""
        return self._Square__size
    
    @size.setter
    def size(self, size):
        """function to set size"""
        try:
            if (size < 0):
                raise ValueError('size must be >= 0')
            self._Square__size = int(size)
        except TypeError:
            raise TypeError("size must be an integer")
    
    def area(self):
        """returns the area of the square"""
        return ((self._Square__size)**2)
