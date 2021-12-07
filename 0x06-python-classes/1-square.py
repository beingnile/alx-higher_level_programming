#!/usr/bin/python3
"""
Class Square defines a square by a private attribute ``size``,
and instantiates with ``size``
"""


class Square:
    """
    Define square with private attribute ``size``
    """
    def __init__(self, size):
        """
        Args:
            size: The size of the square.

        Attributes:
            size: Private instance attribute.
        """
        self.__size = size
