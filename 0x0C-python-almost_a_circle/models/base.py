#!/usr/bin/python3
"""
This script defines a class called Base.
"""


class Base:
    """
    Base class for basic functionality.

    Attributes:
        __nb_objects (int): A class variable
        to keep track of the number of instances.
        id (int): An identifier for each instance.

    Methods:
        __init__(self, id=None): Constructor method
        that initializes an instance with an optional id.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        Base.__nb_objects += 1
        if self.id is None:
            self.id = Base.__nb_objects
        else:
            Base.__nb_objects -= 1
