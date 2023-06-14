#!/usr/bin/python3
"""Defines a function that reads a file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename(str): The file to read and print
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
