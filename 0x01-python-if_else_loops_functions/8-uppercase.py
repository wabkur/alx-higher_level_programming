#!/usr/bin/python3
def uppercase(str):
    besh = ""
    for x in str:
        if ord(x) >= 97 and ord(x) <= 123:
            besh += chr(ord(x) - 32)
            print("{}".format(x), end="")
        print("")
