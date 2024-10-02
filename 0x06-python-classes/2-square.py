#!/usr/bin/python3
"""This is the 1-square module"""


class Square:
    """Creates an instance of the class Square"""

    def __init__(self, size=0):
        """Initializes size with a positive integer value"""
        try:
            if (size < 0):
                raise ValueError('size must be >= 0')
            self._Square__size = size
        except TypeError:
            raise TypeError("size must be an integer")
