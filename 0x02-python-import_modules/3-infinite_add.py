#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number = 0
    for num in sys.argv:
        if num != sys.argv[0]:
            number += int(num)
    print(number)
