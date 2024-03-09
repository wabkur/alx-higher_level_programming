#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        besh = number % 10
    elif number < 0:
        besh = (abs(number) % 10)
    print(besh, end="")
    return besh
