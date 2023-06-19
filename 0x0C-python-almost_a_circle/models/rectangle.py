#!/usr/bin/python3
"""Defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle object"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using # to stdout"""
        if self.y > 0:
            print('\n' * self.y, end='')
        for h in range(self.height):
            if self.x > 0:
                print(' ' * self.x, end='')
            for w in range(self.width):
                print("#", end='')
            print('')

    def __str__(self):
        """Overwrtes __str__ to return a custom string"""
        ret1 = f'[{self.__class__.__name__}] ({self.id}) '
        ret2 = f'{self.x}/{self.y} - {self.width}/{self.height}'

        return ret1 + ret2

    def update(self, *args, **kwargs):
        """Updates the attributes of a rectangle object"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args is None or len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        for i, value in enumerate(args):
            setattr(self, attrs[i], value)
