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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Overwrite __str__ for custom str output"""
        ret1 = f'[{self.__class__.__name__}] ({self.id}) '
        ret2 = f'{self.x}/{self.y} - {self.width}'

        return ret1 + ret2

    def update(self, *args, **kwargs):
        """Updates the Square attributes"""
        attrs = ['id', 'size', 'x', 'y']
        if args is None or len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        for i, value in enumerate(args):
            setattr(self, attrs[i], value)
