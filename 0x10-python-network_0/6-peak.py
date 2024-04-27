#!/usr/bin/python3
"""Defines a function that finds the peak in a list
"""


def find_peak(list_of_integers):
    """Finds the maxim value in a list

    Arguments:
    list_of_integers (list): Integers in a list
    """
    if len(list_of_integers) == 0:
        return None
    return max(set(list_of_integers))
