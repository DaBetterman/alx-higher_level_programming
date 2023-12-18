#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return (value)
    except:
        print("str")
