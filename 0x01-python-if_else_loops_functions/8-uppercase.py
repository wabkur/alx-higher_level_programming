#!/usr/bin/python3
def uppercase(str):
    besh = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            besh += chr(ord(x) - 32)
        else:
        besh += x
        print("{:s}".format(x))
