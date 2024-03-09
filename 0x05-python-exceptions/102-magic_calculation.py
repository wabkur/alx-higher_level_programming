#!/usr/bin/python3
def magic_calculation(a, b):
    number = 0
    for r in range(1, 3):
        try:
            if r > a:
                raise Exception('Too far')
            number += a ** b / r
        except Exception:
            number = b + a
            break
    return number
