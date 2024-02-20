#!/usr/bin/python3
"""Raise class BaseGeometry"""


class BaseGeometry:
    """A class with public instance method and integer_validator value"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
