#!/usr/bin/python3

""" Defines a class Rectangle inheriting from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle """
    def __init__(self, width, height):
        """
        Initialize Rectangle
        Args:
            width (int): The width.
            height (int): The height.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            The print() and str() representation of a Rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
