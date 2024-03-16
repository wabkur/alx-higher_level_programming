#!/usr/bin/python3


# complex_delete - delets keys with a specific value in a dictionary.
def complex_delete(a_dictionary, value):
    klist = []
    if value in a_dictionary.values():
        for key, vals in a_dictionary.items():
            if value == vals:
                klist.append(key)

        for kol in klist:
            if kol in a_dictionary:
                del a_dictionary[kol]
    return a_dictionary
