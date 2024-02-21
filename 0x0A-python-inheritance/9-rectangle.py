#!/usr/bin/python3
""" Area() method gets implemented
    Prints and str returns the description of rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A representation of a rectangle
    Args:
        width (int): rectangle width
        height (int): rectangle height
    """
    def __init__(self, width, height):
        """Initialize and validates width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string representation of Rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
