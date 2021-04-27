#!/usr/bin/python3
for alpha in range(ord('a'), ord('z')+1):
    if alpha == 101 or alpha == 113:
        continue
    print("{:c}".format(alpha), end="")
