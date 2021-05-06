#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if len(sentence) == 0:
        a = None
    b = sentence[0]
    if a != 0:
        return (a, b)
