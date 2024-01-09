#!/usr/bin/python3
"""
This script defines a function that returns
the JSON representation of an object (string).
"""


import json


def from_json_string(my_str):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_str: The object to be converted to JSON.

    Return:
        The JSON representation of the object.
    """
    return json.loads(my_str)
