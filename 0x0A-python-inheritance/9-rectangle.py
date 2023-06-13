#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a Rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Implements the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Overwrites the __str__ method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
