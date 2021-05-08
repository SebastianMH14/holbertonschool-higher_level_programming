#!/usr/bin/python3
def uniq_add(my_list=[]):
    suma = 0
    for i in range(0, len(my_list)):
        if my_list[i] != my_list[2]:
            suma = suma + my_list[i]
    return suma
