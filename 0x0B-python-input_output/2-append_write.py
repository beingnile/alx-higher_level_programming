#!/usr/bin/python3
"""Defines a function that appends a string to a file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename(str): The name of file to append text to
        text(str): The text to append to the file

    Returns:
        (int): The number of characters appended
    """
    with open(filename, 'a', encoding='utf-8') as f:
        app_chars = f.write(text)

    return app_chars
