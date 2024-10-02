#!/usr/bin/python3

"""This is my 5-square module"""


class Square:
    """This creates an istance of the class Square"""

    def __init__(self, size=0):
        """Initializes the object with an integer value"""
        self.size = size

    @property
    def size(self):
        """Gets the size input"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size from user input"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints out a square of size x size dimension"""
        i = 0
        j = 0

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
