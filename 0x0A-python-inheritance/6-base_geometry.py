#!/usr/bin/python3
"""
Module for an empty BaseGeometry.
"""


class BaseGeometry:
    """
    A simple empty class representing the base geometry.
    This class doesn't have any attributes or methods.
    """
    def area(self):
        """
        Raises and exception with a message
        """
        raise Exception("area() is not implemented")
