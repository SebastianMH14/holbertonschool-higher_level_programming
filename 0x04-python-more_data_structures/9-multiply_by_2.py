#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic_t = a_dictionary.copy()
    for i in dic_t:
        dic_t[i] *= 2
    return dic_t
