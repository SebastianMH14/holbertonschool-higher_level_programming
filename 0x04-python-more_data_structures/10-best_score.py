#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    elif len(a_dictionary) == 0:
        return None
    max_score = max(a_dictionary, key=a_dictionary.get)
    return max_score
