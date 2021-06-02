#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r+") as file:
        a = file.read()
        print(a)
