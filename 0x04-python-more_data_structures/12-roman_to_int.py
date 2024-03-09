#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    sets, sum = 0, 0

    for i in roman_string:
        sum += roman_map[i] if roman_map[i] <= stes else roman_map[i] - sets * 2
        sets = roman_map[i]
    return sum
