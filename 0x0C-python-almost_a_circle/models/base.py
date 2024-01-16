#!/usr/bin/python3
import json
import turtle
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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of dictionary objects evaluated from JSON string.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the subclass using that class's
        update method after instantiating one instance.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file.

        Returns:
            list: List of instances.
        """
        cname = cls.__name__

        try:
            with open("{}.json".format(cname), 'r') as myFile:
                text = myFile.read()
        except FileNotFoundError:
            return []

        dict_list = cls.from_json_string(text)

        inst_list = [cls.create(**element) for element in dict_list]

        return inst_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves a list of sub-class objects to their file as CSV.

        Args:
            list_objs (list): List of instances inheriting from Base.
        """
        if list_objs is None:
            list_objs = []

        cname = cls.__name__, list_objs

        super_list = [obj.to_csv() for obj in list_objs]

        write_str = cls.to_csv_lines(super_list)

        with open("{}.csv".format(cname), 'w') as myFile:
            myFile.write(write_str)

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of objects from their CSV file.

        Returns:
            list: List of instances.
        """
        cname = cls.__name__

        try:
            with open(f"{cname}.csv", 'r', encoding='utf-8') as myFile:
                lines = myFile.readlines()
        except FileNotFoundError:
            return []

        csv_list_list = cls.from_csv_lines(lines)

        inst_list = [cls(1, 1) for _ in range(len(csv_list_list))]
        for i, csv_inst in enumerate(csv_list_list):
            inst_list[i].update(*csv_inst)

        return inst_list

    @classmethod
    def get_cname_from_sublist(cls, list_objs):
        """Gets proper cname to use when saving objects.

        Args:
            list_objs (list): List of instances inheriting from Base.

        Returns:
            str: Class name.
        """
        cname = None
        for i, obj in enumerate(list_objs):
            if not issubclass(type(obj), cls):
                continue
            elif cname is None or cname != "Rectangle":
                cname = obj.__class__.__name__
        if cname is None:
            cname = "Rectangle"
        return cname

    @staticmethod
    def to_csv_lines(list_csv):
        """returns CSV string representation from list of sub class
            objects represented in their csv form
        """
        builder = ""
        for csv in list_csv:
            for i, ele in enumerate(csv):
                builder += str(ele)
                if i != len(csv) - 1:
                    builder += ','
            builder += '\n'
        return builder

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        window = turtle.Screen()
        window.bgcolor("white")

        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.color("blue")
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)
            turtle.right(90)
            turtle.forward(rectangle.width)
            turtle.right(90)
            turtle.forward(rectangle.height)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("red")
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)

        turtle.done()
