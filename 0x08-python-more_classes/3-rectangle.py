#!/usr/bin/python3

""" Define rectangle using class Rectangle """


class Rectangle:
    """ Defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        Initialize rectangle.
        Args:
            width(int): The width of the rectangle.
            height(int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Return:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Return:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Return:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Return:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return:
            A printable representation of the Rectangle using #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for h in range(self.__height):
            [rect.append('#') for w in range(self.__width)]
            if h != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
