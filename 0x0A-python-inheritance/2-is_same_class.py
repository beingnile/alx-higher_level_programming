#!/usr/bin/python3

""" Function that checks if object is an instance of a class """


def is_same_class(obj, a_class):
    """
    Args:
        obj: Object to be checked.
        a_class: The class to check the object against.

    Returns:
        True if the obj is an instance of a_class
        False if otherwise.
    """

    if type(obj) == a_class:
        return True
    else:
        return False
