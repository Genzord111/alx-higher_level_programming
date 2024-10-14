#!/usr/bin/python3
"""This module the is_same_class function"""


def is_same_class(obj, a_class):
    """Returns true if the object is exactly an instance of the class"""
    if type(obj) is a_class:
        return True
    else:
        return False
