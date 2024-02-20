#!/usr/bin/python3
"""Raise an exception for non implementation of class BaseGeometry"""


class BaseGeometry:
    """Raise exception with message."""
    def area(self):
        raise Exception("area() is not implemented")
