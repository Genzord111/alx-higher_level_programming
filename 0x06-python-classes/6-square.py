#!/usr/bin/python3

"""This is my 5-square module"""


class Square:
    """This creates an instance of the class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with size and position"""
        self.size = size  # This will call the setter and validate
        self.position = position  # This will call the setter and validate

    @property
    def size(self):
        """Returns the size input"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size from user input with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position input"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position with validation"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(ele, int) and ele >= 0 for ele in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints out a square of size x size dimension"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
