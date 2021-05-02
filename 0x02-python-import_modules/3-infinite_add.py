#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    n = len(argv)
    suma = 0

    for i in range(1, n):
       suma += int(argv[i])
    print(suma)
