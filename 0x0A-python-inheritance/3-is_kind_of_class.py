#!/usr/bin/python3
"""
Module for is_kind_of_class method
"""


def is_kind_of_class(obj, a_class):
    """
    a function that returns True if the object is an instance
    or if the object is an instance of a class that
    inherited from, the specified class ; otherwise False.

    Args:
        obj: (object): the listed object.

    Returns:
        list: if object is True then returns.
    """
    return isinstance(obj, a_class)
