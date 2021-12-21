#!/usr/bin/python3

""" Module with class Square inheriting from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a square """

    def __init__(self, size):
        """
        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
