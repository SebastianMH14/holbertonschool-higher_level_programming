#!/usr/bin/python3
"""function that reads a text file
(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """use the with statement"""
    with open(filename) as file:
        a = file.read()
        print(a, end="")
