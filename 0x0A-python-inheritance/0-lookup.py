#!/usr/bin/python3
def lookup(obj):
    """
    a function that returns the list of available
    attributes and methods of an object
    """
    if not isinstance(obj, list):
        return None
    else:
        return dir(obj)
