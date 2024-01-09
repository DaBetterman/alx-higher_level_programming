#!/usr/bin/python3
"""
This script defines a function that
writes an object to a text
file using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of an object to a text file.

    Args:
        my_obj: The object to be written to the file.
        filename: The name of the file to write to.
    """
    with open(filename, "w") as new_file:
        json.dump(my_obj, new_file)
