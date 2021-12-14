#!/usr/bin/python3

""" Contains class with no class/object attributes """


class LockedClass:
    """
    No class/object attributes

    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called ``first_name``
    """

    __slots__ = ["first_name"]
