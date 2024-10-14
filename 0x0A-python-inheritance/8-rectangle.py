"""This module contains Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle  inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes and validates protected attributes"""

        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)