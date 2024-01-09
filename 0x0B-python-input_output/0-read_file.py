#!/usr/bin/python3
"""
A module with a function read_file.
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout:
    """
    with open(filename, "r") as new_file:
        new_files = new_file.read()
        print(new_files)
