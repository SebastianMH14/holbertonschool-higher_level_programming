#!/usr/bin/python3
"""writes a string to a text file
(UTF8) and returns the
number of characters written
"""


def append_write(filename="", text=""):
    """use the with statement"""
    with open(filename, 'a', encoding="utf-8") as file:
        a = file.write(text)
        return a
