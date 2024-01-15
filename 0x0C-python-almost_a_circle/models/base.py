#!/usr/bin/python3
import json
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
        """
        Constructor method for the Base class.

        Args:
            id (int, optional): An identifier for
            the instance. Defaults to None.
        """
        self.id = id

        Base.__nb_objects += 1
        if self.id is None:
            self.id = Base.__nb_objects
        else:
            Base.__nb_objects -= 1

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries
        to a JSON-formatted string.

        Args:
            list_dictionaries (list): A
            list of dictionaries.

        Returns:
            str: A JSON-formatted string.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write(cls.to_json_string([]))
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))
