#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Writes text to a file. If file doesn't exist, one
    is created. The function overwrites the content of the
    file if already exists

    Args:
        filename(str): The file to write to
        text(str): The text to write into `filename`

    Returns:
        (int): Number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        written_chars = f.write(text)

    return written_chars
