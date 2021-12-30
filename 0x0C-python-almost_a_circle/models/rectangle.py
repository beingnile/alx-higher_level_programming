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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
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
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Get x value"""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Get y value"""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        Returns:
            The area of the rectangle defined by class Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Returns:
            A Visual representation of the rectangle using # symbols
        """
        for emptyline in range(self.__y):
            print('')
        for newline in range(self.__height):
            for space in range(self.__x):
                print(' ', end = '')
            for symbol in range(self.__width):
                print("#", end='')
            print('')

    def __str__(self):
        """
        Returns:
            The overridden __str__ method
        """
        return (f"[Rectangle] " + f"({self.id}) {self.__x}/"
                + f"{self.y} - {self.__width}/{self.__height}")
