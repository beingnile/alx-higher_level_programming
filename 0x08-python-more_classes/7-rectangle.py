#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height attribute value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints the rectangle to stdout"""
        if self.width == 0 or self.height == 0:
            return ''
        for i in range(self.height):
            for j in range(self.width):
                print(str(Rectangle.print_symbol), end='')
            if i == self.height - 1:
                return ''
            print('')

    def __repr__(self):
        """Prints the string representation of the object.
        The representation can be converted back into an object
        using eval()
        """
        return f"{self.__class__.__name__}({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __setattr__(self, name, value):
        if name == "print_symbol":
            self.__class__.print_symbol = value
        else:
            super().__setattr__(name, value)
