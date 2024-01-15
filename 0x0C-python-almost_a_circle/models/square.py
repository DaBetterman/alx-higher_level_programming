#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This script defines a class called Rectangle.
"""


class Square(Rectangle):
    """
    Square class, inherited from Rectangle.

    Attributes:
        All attributes are inherited from the Rectangle class.

    Methods:
        __init__(self, size, x=0, y=0, id=None): Constructor
                                method for the Square class.
        __str__(self): Return a string representation of the square.
        size (property): Getter method for the size attribute.
        size (setter): Setter method for the size attribute.
        update(self, *args, **kwargs): Update the attributes of the square.
        to_dictionary(self): Convert the square's attributes to a dictionary.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for the Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): The x-coordinate of
                                the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the
                                square's position. Defaults to 0.
            id (int, optional): The unique identifier of
                                the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A formatted string representing the square's information.
        """
        return "[{}] ({}) {}/{} - \
{}".format(__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter method for size.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): New size for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.

        Args:
            *args: Variable length argument list
                    containing values for id, size, x, and y.
            **kwargs: Arbitrary keyword arguments
                    containing values for id, size, x, and y.
        """
        if args:
            attr = ['id', 'size', 'x', 'y']
            for index, arg in enumerate(args):
                setattr(self, attr[index], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the square's attributes to a dictionary.

        Returns:
            dict: A dictionary containing the square's id, size, x, and y.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
