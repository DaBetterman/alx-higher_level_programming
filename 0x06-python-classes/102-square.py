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
        area(self): Calculates and returns the area of the square.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
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

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
