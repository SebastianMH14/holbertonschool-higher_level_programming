#!/usr/bin/python3
"""function that returns the list
 of available attributes and methods
 of an object"""


def lookup(obj):
    """create a funtion with dir"""
    a = list(dir(obj))
    return a
