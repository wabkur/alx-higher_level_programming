#!/usr/bin/python3
"""Raise a class BaseGeometry and subclass rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A representation of a rectangle
    rectangle width
    rectangle height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
