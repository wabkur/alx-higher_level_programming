#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for gets in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(gets, a_dictionary[gets]))
