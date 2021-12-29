#!/usr/bin/python3

from base import Base
"""Defines a Class rectangle that inherits from the base class"""


class Rectangle(Base):
    """Class Rectangle defines a rectangle and inherits from base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the object on instantiation

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): x
            y (int): y
        """
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """Get x value"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Get y value"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
