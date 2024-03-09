#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for get in matrix:
        new.append([x ** 2 for x in get])
    return new
