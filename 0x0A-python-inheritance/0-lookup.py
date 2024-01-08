#!/usr/bin/python3
"""
Module for looking up a method
"""


def lookup(obj):
    """
    a function that returns the list of available
    attributes and methods of an object.

    Args:
        obj: (object): the listed object.

    Returns:
        list: the list to be printed.
    """
    return dir(obj)
