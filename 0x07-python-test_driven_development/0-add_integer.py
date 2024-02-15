#!/usr/bin/python3
""" A function that add two integers"""
def add_integer(a, b=98):
    """Raises TypeError with corresponding message if a or b
    is not an int or a float
    """
    if type(a) is not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not in [int, float]:
        raise TypeError("b most be an integer")
    return int(a) + int(b)
