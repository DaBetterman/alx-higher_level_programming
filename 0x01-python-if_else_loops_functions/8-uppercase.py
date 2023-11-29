#!/usr/bin/python3
def uppercase(up):
    result = ""
    for char in up:
        if 97 <= ord(char) and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
