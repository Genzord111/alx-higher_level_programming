#!/usr/bin/python3
"""This module contains the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This  class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of width, height, x and y"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def dimension_validator(self, name, dimension, greater_than_zero):
        """checks if para is integer and non zero"""
        if not isinstance(dimension, int):
            raise TypeError(f"{name} must be an integer")
        if dimension <= 0 and greater_than_zero is True:
            raise ValueError(f"{name} must be > 0")
        if dimension < 0 and greater_than_zero is False:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        """Returns width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width attribute"""
        self.dimension_validator("width", width, True)
        self.__width = width

    @property
    def height(self):
        """Returns height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height attribute"""
        self.dimension_validator("height", height, True)
        self.__height = height

    @property
    def x(self):
        """Returns x attribute"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x attribute"""
        self.dimension_validator('x', x, False)
        self.__x = x

    @property
    def y(self):
        """Returns y attribute"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y attribute"""
        self.dimension_validator('y', y, False)
        self.__y = y

    def __str__(self):
        """Returns the class and it's attributes as string"""

        return f'[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}'

    def area(self):
        """calculates area"""
        return self.__width * self.__height

    def display(self):
        """displays rectangle/square to stdout"""
        for i in range(self.__y):
            print('')
        for j in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def update(self, *args, **kwargs):
        """updates the values of instance attributes"""
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]

            return

        else:
            if kwargs.get("id") is not None:
                self.id = kwargs.get("id")
            if kwargs.get("width") is not None:
                self.width = kwargs.get("width")
            if kwargs.get("height") is not None:
                self.height = kwargs.get("height")
            if kwargs.get("x") is not None:
                self.x = kwargs.get("x")
            if kwargs.get("y") is not None:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return (
                {'x': self.x,
                 'y': self.y,
                 'id': self.id,
                 'height': self.height,
                 'width': self.width}
        )
