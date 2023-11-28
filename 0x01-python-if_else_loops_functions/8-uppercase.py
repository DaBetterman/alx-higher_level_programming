#!/usr/bin/python3
for i in range(0, 10):
    for numb in range(i + 1, 10):
        print("{}{}".format(i, numb), end=", " if i < 8 or numb < 9 else "\n")
