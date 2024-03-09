#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        get = 0
        for r in range(x):
            print(my_list[r], end="")
            get += 1
            for x in range(get):
                print("", end="")
        print()
        return get
    except IndexError:
        print()
        return get
