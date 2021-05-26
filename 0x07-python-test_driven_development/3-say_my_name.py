#!/usr/bin/python3
""" function that prints
My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """first_name and last_name must be strings
    otherwise, raise a TypeError exception with the message
    irst_name must be a string or last_name must be a string"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    else:
        print("My name is {:s}".format(first_name), end=" ")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("{:s}".format(last_name))
