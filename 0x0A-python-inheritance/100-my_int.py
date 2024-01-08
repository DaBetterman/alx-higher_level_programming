#!/usr/bin/python3
"""
A class MyInt that inherits from int:
"""


class MyInt(int):
    """
    A class representing MyInt that inherits from int.
    """

    def __eq__(self, nameless):
        """
        Overrides the == operator.
        """
        return super().__ne__(nameless)

    def __ne__(self, nameless):
        """
        Overrides the != operator.
        """
        return super().__eq__(nameless)
