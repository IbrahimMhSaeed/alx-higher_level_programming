#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    max_v = float('-inf')
    for key, val in a_dictionary.items():
        if val > max_v:
            max_v = val
            name = key
    return (name)
