#!/usr/bin/python3
import json
import turtle
"""
This script defines a class called Base.
"""


class Base:
    """
    Base class for basic functionality.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the Base class.
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
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.
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
        """
        if json_string is None or len(json_string) == 0:
            return []
        return eval(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the subclass using that class's
        update method after instantiating one instance.
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
        """
        Loads a list of objects from their CSV file.
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
        """
        Gets proper cname to use when saving objects.
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
        """
        returns CSV string representation from list of sub class
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
        """
        Opens a window and draws all the Rectangles and Squares.
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
