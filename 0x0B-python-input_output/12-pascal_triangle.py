#!/usr/bin/python3
"""Defines a function pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the Pascal's
    triangle of n

    Args:
        n(int): The height of the triangle

    Returns:
        (list): List of lists of integers representing the Pascal's
        triangle of n
    """
    res = []
    if n <= 0:
        return res
    row = [1]
    res.append(row)
    next_row = []
    for i in range(1, n):
        row = [0] + row + [0]
        for j in range(len(row)):
            next_row[j] = row[j] + row[j + 1]
        res.append(next_row)
        row = next_row

    return res
