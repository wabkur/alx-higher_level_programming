#!/usr/bin/python3
"""implement the size attribute and subclass Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation a square from the rectangle"""
    def __init__(self, size):
        """initialize size of a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
