#!/usr/bin/python3
def fizzbuzz():
    for besh in range(1, 101):
        if besh % 3 == 0 and besh % 5 == 0:
            print("FizzBuzz", end=" ")
        elif besh % 3 == 0:
            print("Fizz", end=" ")
        elif besh % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(besh, end=" ")
