#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        besh = a / b
    except ZeroDivisionError:
        besh = None
    finally:
        print("Inside result:", "{}".format(besh))
        return besh
