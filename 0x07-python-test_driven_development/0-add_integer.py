#!/usr/bin/python3
""" this contains func. that add two int values"""

def add_integer(a, b=98):
    """Raises TypeError with corresponding message if a or b
    is not an int or a float
    """
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b most be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

