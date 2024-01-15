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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def display(self):
        """
        Display the rectangle by printing '#' characters.

        Note:
            This method prints the
            rectangle's position and dimensions.
        """
        # for i in range(self.height):
        #     for j in range(self.width):
        #         print("#", end="")
        #     print("")

        for i in range(self.y):
            print("")

        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A formatted string
            representing the rectangle's information.
        """
        name = self.__class__.__name__
        return "[{}] ({}) {}/{} - {}/{}\
".format(name, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: Variable length argument list
                    containing values for id,
                    width, height, x, and y.
            **kwargs: Arbitrary keyword arguments
                    containing values for
                    id, width, height, x, and y.
        """
        if args:
            attr = ['id', 'width', 'height', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, attr[index], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the rectangle's attributes to a dictionary.

        Returns:
            dict: A dictionary containing the
            rectangle's id, width, height, x, and y.
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
