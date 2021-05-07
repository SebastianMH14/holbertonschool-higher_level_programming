#!/usr/bin/python3
def no_c(my_string):
    counts_c = my_string.count("c")
    counts_C = my_string.count("C")
    if counts_c > 0:
        my_string = list(my_string)

        while counts_c:
            my_string.remove("c")
            counts_c -= 1
        my_string = ''.join(my_string)
    if counts_C > 0:
        my_string = list(my_string)

        while counts_C:
            my_string.remove("C")
            counts_C -= 1
        my_string = ''.join(my_string)
    return my_string
