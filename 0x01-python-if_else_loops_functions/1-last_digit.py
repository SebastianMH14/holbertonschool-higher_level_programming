#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = number % 10
j = -1
if number < 0:
    i = number * j
    x = i % 10 * -1
if x > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, x))
else:
    print("Last digit of {} is {} and\
 is less than 6 and not 0".format(number, x))
