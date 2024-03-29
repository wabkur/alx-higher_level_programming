#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def arg_calc(argv):
    r = len(argv) - 1
    if r != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    opp = argv[2]
    b = int(argv[3])
    if opp == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, opp, b, add(a, b)))
    elif opp == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, opp, b, sub(a, b)))
    elif opp == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, opp, b, mul(a, b)))
    elif opp == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, opp, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    import sys
    arg_calc(sys.argv)
