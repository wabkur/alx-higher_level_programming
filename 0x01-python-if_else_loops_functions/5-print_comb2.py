#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(i)
    else:
        print('{},'.format(str(i).zfill(2)), end=' ')
