#!/usr/bin/python3
"""Defines a function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds 2 integers

    Args:
    a(int): First integer. if not int, raise TypeError
    b(int): Second integer, if not int, raise TypeError

    Returns: The sum of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
