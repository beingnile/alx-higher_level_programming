#!/usr/bin/python3

"""
Function that checks if object is an inherited instance of a class
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: Object to be checked.
        a_class: The specified class.
    Returns:
        True if the obj is an inherited instance of a_class
        False if otherwise.
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
