#!/usr/bin/python3
"""This module contains a add_integer function"""


def add_integer(a, b=98):
    """Returns the addition of 2 integers or floats as integer
    Parameters: a,b (int): Integers or floating point numbers
    Returns: Integer result of addition of a and b"""

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result
