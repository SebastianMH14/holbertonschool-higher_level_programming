#!/usr/bin/python3
"""function that returns True if
the object is exactly an instance
of the specified class"""


def is_same_class(obj, a_class):
    """check if it is the same"""
    if type(obj) == a_class:
        return True
    else:
        return False
