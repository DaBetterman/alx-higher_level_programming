#!/usr/bin/python3
from models.rectangle import Rectangle
"""
This script defines a class called Rectangle.
"""


class Square(Rectangle):
    """
    Square class, inherited from Rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for the Square class.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the square.
        """
        return "[{}] ({}) {}/{} - \
{}".format(__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the attributes of the square.
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
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def to_csv(self):
        """
        Returns CSV string representation of the Square object.
        """
        return "{},{},{},{}".format(self.id, self.size, self.x, self.y)
