#!/usr/bin/python3
def best_score(a_dictionary):
    count = 0
    best_score = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > count:
                count = value
                best_score = key
    return (best_score)
