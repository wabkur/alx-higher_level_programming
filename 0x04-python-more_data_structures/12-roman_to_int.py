#!/usr/bin/python3
def roman_to_int(roman_string):
    get = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
            }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sets, sum = 0, 0

    for r in roman_string:
        sum += get[r] if get[r] <= sets else get[r] - sets * 2
        sets = get[r]
    return sum
