#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    ar = sys.argv
    lenAv = len(sys.argv)
    if lenAv != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if ar[2] != '+' and ar[2] != '-' and ar[2] != '*' and ar[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(ar[1])
    b = int(ar[3])
    if ar[2] == '+':
        print(a, ar[2], b, "=", add(a, b))
    if ar[2] == '-':
        print(a, ar[2], b, "=", sub(a, b))
    if ar[2] == '*':
        print(a, ar[2], b, "=", mul(a, b))
    if ar[2] == '/':
        print(a, ar[2], b, "=", div(a, b))
