#!/usr/bin/python3

"""
Defines a Class rectangle that inherits from the class Base in base module
"""
from models.base import Base


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
        if type(width) != int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        if type(height) != int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        if type(x) != int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        if type(y) != int:
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
        if type(width) != int:
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
        if type(height) != int:
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
        if type(x) != int:
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
        if type(y) != int:
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
                print(' ', end='')
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

    def update(self, *args, **kwargs):
        """Updates the class Rectangle attributes
        Args:
            *args (int): The values replacing the attributes
            **kwargs (dict): Key, Value pairs of the attributes
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    if type(arg) != int:
                        raise TypeError('width must be an integer')
                    elif arg <= 0:
                        raise ValueError('width must be > 0')
                    self.__width = arg
                elif index == 2:
                    if type(arg) != int:
                        raise TypeError('height must be an integer')
                    elif arg <= 0:
                        raise ValueError('height must be > 0')
                    self.__height = arg
                elif index == 3:
                    if type(arg) != int:
                        raise TypeError('x must be an integer')
                    elif arg < 0:
                        raise ValueError('x must be >= 0')
                    self.__x = arg
                elif index == 4:
                    if type(arg) != int:
                        raise TypeError('y must be an integer')
                    elif arg < 0:
                        raise ValueError('y must be >= 0')
                    self.__y = arg
                index += 1

        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    if type(v) != int:
                        raise TypeError('width must be an integer')
                    elif v <= 0:
                        raise ValueError('width must be > 0')
                    self.__width = v
                elif k == "height":
                    if type(v) != int:
                        raise TypeError('height must be an integer')
                    elif v <= 0:
                        raise ValueError('height must be > 0')
                    self.__height = v
                elif k == "x":
                    if type(v) != int:
                        raise TypeError('x must be an integer')
                    elif v < 0:
                        raise ValueError('x must be >= 0')
                    self.__x = v
                elif k == "y":
                    if type(v) != int:
                        raise TypeError('y must be an integer')
                    elif v < 0:
                        raise ValueError('y must be >= 0')
                    self.__y = v

    def to_dictionary(self):
        """Return the dictionary representation of attributes"""
        return {
                "id": self.id,
                "width": self.__width,
                "height": self.__height,
                "x": self.__x,
                "y": self.__y
                }
