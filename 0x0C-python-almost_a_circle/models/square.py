#!/usr/bin/python3

from models.rectangle import Rectangle
"""Defines a class Square that inherits from class Rectangle"""


class Square(Rectangle):
    """Defines a square and inherits attributes from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the object on instantiation

        Args:
            size (int): The Length and Width of the square object
            x (int): x axis
            y (int): y axis
            id (int): The identification
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the inbuilt __str__ method

        Returns:
            A custom str for __str__ method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
