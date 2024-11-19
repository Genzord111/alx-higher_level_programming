#!/usr/bin/python3
"""This module contains the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This square class inherits from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class instantiation"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns square size value"""
        return self.width

    @size.setter
    def size(self, size):
        """Sets the value of square size"""
        self.dimension_validator("width", size, True)
        self.width = size
        self.height = size

    def __str__(self):
        """Returns the class and it's attributes as string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """updates the values of instance attributes"""
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
            return
        else:
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("size") is not None:
                self.width = kwargs.get("size")
                self.height = kwargs.get("size")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """ returns the dictionary representation of a Square's attribute"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
