#!/usr/bin/python3
from typing import no_type_check


def multiply_list_map(my_list=[], number=0):
    return list(map((lambda x: x * number), my_list))
