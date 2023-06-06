#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """Prints a square of size size

    Args:
        size(int): The size of the square to print
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print('')
        return
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print('')
