#!/usr/bin/python3
"""
This script defines a function that creates an object from a JSON file.
"""


import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.

    Args:
        filename: The name of the JSON file.

    Return:
        The Python object created from the JSON file.
    """
    with open(filename, "r") as new_file:
        temp = json.load(new_file)
    return temp
