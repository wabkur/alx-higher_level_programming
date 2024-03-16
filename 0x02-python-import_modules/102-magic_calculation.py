#!/usr/bin/python3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        r = add(a, b)
        for p in range(4, 6):
            r = add(c, p)
        return (r)
    else:
        return(sub(a, b))
