#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for i in range(0, len(my_list)):
        if my_list[i] == i:
            False
        else:
            suma = suma + my_list[i]
    return suma + 1