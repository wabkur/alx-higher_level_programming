#!/usr/bin/python3
"""check if obj is exactly an instance of the class"""
def is_same_class(obj, a_class):
    """If object is exactly an instance of a_class - True.
    otherwise - False.
    """
    return True if type(obj) is a_class else False
