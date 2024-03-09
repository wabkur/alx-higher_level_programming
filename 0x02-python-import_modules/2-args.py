#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    w = len(sys.argv) - 1

    if w == 0:
        print("{} arguments.".format(w))
    elif w == 1:
        print("{} argument:".format(w))
    else:
        print("{} arguments:".format(w))

    if w >= 1:
        w = 0
        for arg in sys.argv:
            if w != 0:
                print("{}: {}".format(w, arg))
            w += 1
