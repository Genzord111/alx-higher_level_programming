#!/usr/bin/python3
"""This module inherits_from function"""


def inherits_from(obj, a_class):
    """Returns true if object isinstance of subclass but not cls"""

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
