#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    besh = 0

    for b in range(x):
        try:
            print("{:d}".format(my_list[b]), end='')
        except TypeError:
            pass
        except ValueError:
            pass
        else:
            besh = besh + 1

    print()
    return (besh)
