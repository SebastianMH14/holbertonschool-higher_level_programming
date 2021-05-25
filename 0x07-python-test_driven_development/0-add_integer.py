#!/usr/bin/python3
"""function that adds 2 integers.
    a and b must be integers or floats, 
    otherwise raise a TypeError exception 
    with the message a must be an integer or b 
    must be an integer"""


def add_integer(a, b=98):
    """returns the sum of two integers a
    and b and a y b must be a float or integers
    if not raise error"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)): 
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
