#!/usr/bin/python3

def best_score(a_dictionary):
    key, value = None, 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v >= value:
                key, value = k, v
    return key
