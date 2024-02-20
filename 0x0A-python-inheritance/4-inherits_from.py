#!/usr/bin/python3
"""contain the inherits_from function that checks for only subclass"""


def inherits_from(obj, a_class):
    """Return True if obj is a subclass of a_class, otherwise false"""
    if (issubclass(type(obj), a_class) and type(obj) != a_class)
        return True
    return False
