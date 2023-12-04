#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count == 0:
        count = None
    first_letter = sentence[0]
    return (count, first_letter)
