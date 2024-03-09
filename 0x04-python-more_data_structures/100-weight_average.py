#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        wgt = 0
        dm = 0
        avr = 0
        for r in range(len(my_list)):
            for p in range(len(my_list[r])):
                wgt += my_list[r][0] * my_list[r][1]
                dm += my_list[r][1]
        avr = wgt / dm
        return avr
    return 0
