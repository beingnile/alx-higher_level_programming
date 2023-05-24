#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square object"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square"""
        return self.size * self.size

    def my_print(self):
        """Prints a drawing of the square"""
        if self.size == 0:
            print('')
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print('')
