#!/usr/bin/python3
def uppercase(up):
    for char in up:
        if 97 <= ord(char) <= 122:
            print("{}".format(chr(ord(char) - 32)), end="")
        else:
            print("{}".format(char), end="")
print("")


