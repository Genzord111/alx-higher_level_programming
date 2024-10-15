#!/usr/bin/python3
"""This module contains class_to_json function"""


class Student:
    """This creates a class of student details"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            new = {}
            for ele in attrs:
                for keys, value in self.__dict__.items():
                    if keys == ele:
                        new[keys] = value
            return new
