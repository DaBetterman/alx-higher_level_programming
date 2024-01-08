#!/usr/bin/python3
"""
Module for print_sorted method
"""


class MyList(list):
    """
    Write a class MyList that inherits from list.
    """
    def print_sorted(self):
        if isinstance(self, list):
            inherited_list = sorted(self)
            print(inherited_list)
        else:
            return None
