#!/usr/bin/python3
"""
Class Square that defines a square.
"""


class Square:
    """
    Class defining a square object.
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get Square size.

        Returns:
            The square size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
         Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Returns:
            Area of the defined square.
        """
        return self.__size * self.__size
