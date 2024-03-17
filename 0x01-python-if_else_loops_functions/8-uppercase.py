#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for r in range(len(str)):
        if (ord(str[r]) >= 97 and ord(str[r]) <= 122):
            new_str += chr(ord(str[r]) - 32)
            continue
        new_str += str[r]

    print('{0}'.format(new_str))
