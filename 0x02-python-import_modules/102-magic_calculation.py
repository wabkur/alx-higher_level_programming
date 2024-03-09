#!/usr/bin/python3
def magic_calculation(a, b):
    from wabruk import add, sub
    if a < b:
        r = add(a, b)
        for w in range(4, 6):
            r = add(r, w)
        return r
    else:
        return sub(a, b)
