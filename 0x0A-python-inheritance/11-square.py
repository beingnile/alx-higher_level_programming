#!/usr/bin/python3
"""Defines a Square class that inherits from the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a Square object"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Overwrites the __str__ method"""
        return f"[Square] {self.__size}/{self.__size}"
