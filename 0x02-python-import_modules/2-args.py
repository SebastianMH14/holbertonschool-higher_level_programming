#!/usr/bin/python3
from sys import argv
n = len(argv)

if n == 1:
    print("0 arguments.")
    if n == 2:
        print("{:d} argument: ".format(n - 1))
else:
    print("{:d} arguments: ".format(n - 1))
    for i in range(1, n):
        print("{:d}:".format(i), argv[i])
