#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    for num in set(my_list):
        summ = summ + num
    return summ
