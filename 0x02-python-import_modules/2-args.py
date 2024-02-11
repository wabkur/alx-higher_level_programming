#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num = len(args) - 1
    if num == 0:
        print("0 arguments:")
    elif num == 1:
        print("1 argurment:")
    else:
        print("{} argurments:".format(num))
        for i in range(num):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
