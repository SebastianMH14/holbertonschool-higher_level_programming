#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for i in range(len(str)):
        if n == i:
            continue
        str1 += str[i]
    return str1
