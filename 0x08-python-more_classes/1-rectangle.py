#!/usr/bin/python3
"""A Rectangle class"""

class Rectangle:
    """Class representing a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.
        
        Parameter:
            int(width) = The width value of the new rectangle.
            int(height) = The height value of the new rectangle
        """
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
