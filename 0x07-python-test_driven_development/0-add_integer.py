#!/usr/bin/python3

def add_integer(a, b=98):
    if type(a) is not int and float:
        raise TypeError("a must be an integer")
    if type(b) is not int and float:
        raise TypeError("b most be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

