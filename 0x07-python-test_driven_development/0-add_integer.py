#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.
    
    Parameter:
    @a: First integer
    @b: Second integer

    Returns:
    Interger: the addition of a and b

    Raises:
    TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    result = int(a) + int(b)
    return result
