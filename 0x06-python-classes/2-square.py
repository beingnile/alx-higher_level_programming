#!/usr/bin/python3
"""
Class Square that defines a square by:
    * Private instance attribute ``size``.
    * Instantiation with optional size.
If size is not an integer, Square raises a ``TypeError``
exception with the message ``size must be an integer``.
If size is less than 0, a ``ValueError`` exception
with the message ``size must be >= 0`` is raised.
"""


class Square:
    """
    Class defining a square object.
    """
    def __init__(self, size=0):
        """
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        self.__size = size
        if isinstance(size, int):
            pass
        else:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
