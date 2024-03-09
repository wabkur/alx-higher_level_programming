#!/usr/bin/python3
def remove_char_at(str, n):
    w = ""
    for i in range(len(str)):
        if i != n:
            w = w + str[i]
    return (w)
