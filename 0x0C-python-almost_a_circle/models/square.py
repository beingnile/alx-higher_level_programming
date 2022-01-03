#!/usr/bin/python3

"""
Defines a class Square that inherits from class Rectangle
"""
from models.rectangle import Rectangle


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

    @property
    def size(self):
        """Gets the size of the square"""
        return self.height

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """Overrides the inbuilt __str__ method

        Returns:
            A custom str for __str__ method
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """Updates the attributes of class square

        Args:
            *args (int): A list of non-keyworded arguments
            **kwargs (int): A list of keyworded arguments
        """
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1

        else:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return a dictionary representation of a Square"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
