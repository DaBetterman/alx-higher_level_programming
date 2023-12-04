#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    if count == 0:
        first_letter = None
    else:
        first_letter = sentence[0]
    return (count, first_letter)
