#!/usr/bin/python3
"""This module creates an inheritable class"""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
