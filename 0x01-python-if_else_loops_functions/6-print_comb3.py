#!/usr/bin/python3
for x in range(10):
    for j in range(10):
        if x != j and (x < j) and ((x * 10) + j) < 89:
            print("{:d}{:d}".format(x, j), end=", ")
        elif ((x * 10) + j) == 89:
            print("{:d}{:d}".format(x, j))