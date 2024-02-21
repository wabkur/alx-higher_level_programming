#!/usr/bin/python3
"""contain the class BaseGeometry and subclass rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define a square class"""
    def __init__(self, size):
        """initialize and validate attributes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
