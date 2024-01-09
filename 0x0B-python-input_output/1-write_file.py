#!/usr/bin/python3
"""
This script defines a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """
    Write the given text to the specified file.

    Args:
        filename: The name of the file to write to.
        text: The text to be written to the file.
    Return:
        The number of bytes written to the file.
    """
    with open(filename, "w") as new_file:
        return new_file.write(text)
