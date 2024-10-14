#!/usr/bin/python3
"""This module the is_kindof_class function"""


def is_kind_of_class(obj, a_class):
    """Returns true if the object is an instance of inherited class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
