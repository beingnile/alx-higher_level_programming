#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square object"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Overwrite __str__ method"""
        return f"[Rectangle] {self.__size}/{self.__size}"
