#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    r = 0
    get = []
    while r < list_length:
        tes = 0
        try:
            tes = my_list_1[r] / my_list_2[r]
        except ZeroDivisionError:
            print("divide by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of a range")
        finally:
            get.append(tes)
            r += 1
    return ret
