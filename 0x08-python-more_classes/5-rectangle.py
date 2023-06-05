#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a Rectangle object"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Overwrites __str__ method to print the rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        for i in range(self.height):
            for j in range(self.width):
                print("#", end='')
            if i == self.height - 1:
                return ''
            print('')

    def __repr__(self):
        """Return a string representation of the object

        ::
            The output can be reconstructed back into an object
        ::
        """
        return f"{self.__class__.__name__}({self,width}, {self.height})"

    def __del__(self):
        """Prints a  message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
