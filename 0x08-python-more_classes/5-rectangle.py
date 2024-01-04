#!/usr/bin/python3
"""Defines a Rectangle class.

This class represents a rectangle with width and height properties.
"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: The width of the new rectangle.
            height: The height of the new rectangle.
        """
        self.width = width
        self.height = height

    def __del__(self):
        """ called when a rectangle instance is deleted """
        print("Bye rectangle...")

    @property
    def width(self):
        """Getter/setter the width of the rectangle. (Private Instance)"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter the height of the rectangle. (Private Instance)"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area of the rectangle (Public instance)"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returning the parameter of the rectangle (Public Instance)"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        string = ""
        for i in range(self.__height):
            for _ in range(self.__width):
                string += '#'
            if i != self.__height - 1:
                string += '\n'
        return (string)

    def __repr__(self):
        """ provides __repr__ method for object when repr()
            is called, or eval().
        """
        string = "Rectangle("
        string += str(self.width)
        string += ", " + str(self.height) + ")"
        return string
