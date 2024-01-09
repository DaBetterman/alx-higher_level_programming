#!/usr/bin/python3
"""
A module with a function read_file.
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout:
    Args:
        @filename: contains string from a file.

    Returns:
        Nothing
    """
    with open(filename, "r") as file:
        print(file.read())
