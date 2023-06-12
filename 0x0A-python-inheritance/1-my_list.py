#!/usr/bin/python3
"""Defines a class MyList with a public instance
method print_sorted()"""


class MyList(list):
    """Inherits from list type"""
    def print_sorted(self):
        """Prints a sorted list object"""
        print(sorted(self))
