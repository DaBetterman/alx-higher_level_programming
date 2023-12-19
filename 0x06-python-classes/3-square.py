#!/usr/bin/python3

"""
This module defines the Square class.

It provides a basic representation of a square.
"""


class Square:
    """
    This is the Square class.

    Attributes:
        __size (int): The size of the square. Default is 0.

    Methods:
        __init__(self, size=0): Initializes a new instance of the Square class.
            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
    """
    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
