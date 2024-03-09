#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for get in my_list:
        if get == search:
            get = replace
        new.append(get)
    return new
