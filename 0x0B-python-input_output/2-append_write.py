#!/usr/bin/python3
"""
This script defines a function for appending text to a file.
"""


def append_write(filename="", text=""):
    """
    Append the given text to the specified file.

    Args:
        filename: The name of the file to append to.
        text: The text to be written to the file.
    Return:
        The number of bytes written to the file.
    """
    with open(filename, "a") as new_file:
        return new_file.write(text)
