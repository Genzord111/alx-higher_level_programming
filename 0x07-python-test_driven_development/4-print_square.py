#!/usr/bin/python3
"""This module contains a function to print a square made of #"""


def print_square(size):
    """Prints out a square of size x size dimension"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
