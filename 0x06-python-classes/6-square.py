#!/usr/bin/python3

"""This is my 5-square module"""


class Square:
    """This creates an istance of the class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the object integer values"""
        self.__size = size
        self.__position =  position

    @property
    def size(self):
        """Returns the size input"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size from user input"""
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
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")


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
            if self.__position[1] > 0:
                print("")

            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print("_",end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
