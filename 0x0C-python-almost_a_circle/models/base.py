#!/usr/bin/python3
"""This module contains the Base class"""


class Base:
    """This is the base class for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation with id or num of onject"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
