#!/usr/bin/python3
from models.base import Base
"""
Module for Rectangle class
"""


class Rectangle(Base):
    """
    Rectangle class inheriting from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        return self.__height, value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        return self.__x, value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        return self.__y, value
