#!/usr/bin/python3
"""
Module for looking up a method
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object
    is exactly an instance of the
    specified class ; otherwise False.
    """
    temp = type(obj) is a_class
    return temp
