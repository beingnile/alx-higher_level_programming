#!/usr/bin/python3
"""Defines a function lookup()"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object

    Args:
        obj(any): An object of any type
    """
    return dir(obj)
