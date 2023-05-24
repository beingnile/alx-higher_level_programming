#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square object"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get the square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square size"""
        if not isinstance(value, size):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Get the square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the square position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square's area"""
        return self.size * self.size

    def my_print(self):
        """Prints the square to stdout with the characters #"""
        if self.size == 0:
            print('')
        for i in range(self.size):
            print(' ' * self.position[0], end='')
            for j in range(self.size):
                print("#", end='')
            print('')
