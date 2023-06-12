#!/usr/bin/python3
"""Defines a function is_same_class()"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the
    specified class

    Args:
        obj(any): An object of any type
        a_class(any): Class to check object against

    Returns:
        True is obj is of type a_class, otherwise False
    """
    if a_class == object:
        return False
    return isinstance(obj, a_class)
