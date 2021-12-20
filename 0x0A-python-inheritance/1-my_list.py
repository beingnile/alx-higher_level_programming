#!/usr/bin/python3

""" Defines a class MyList that inherits from list """


class MyList(list):
    """
    Uses buitin list methods to print sorted list
    """
    def print_sorted(self):
        """ Prints a sorted list """
        print(sorted(self, reverse=False))
