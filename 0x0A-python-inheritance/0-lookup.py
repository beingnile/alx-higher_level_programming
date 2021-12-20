#!/usr/bin/python3

"""
Return list of available attributes and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj (object): The object.
    Returns:
        A list of available attributes and methods of an object.
    """
    return dir(obj)
