#!/usr/bin/python3
"""Defines a square class inheriting from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square object"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """Overwrite __str__ for custom str output"""
        ret1 = f'[{self.__class__.__name__}] ({self.id}) '
        ret2 = f'{self.x}/{self.y} - {self.width}'

        return ret1 + ret2
