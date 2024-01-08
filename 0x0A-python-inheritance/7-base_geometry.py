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

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
