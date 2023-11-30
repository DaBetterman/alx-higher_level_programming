#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arg_count = len(sys.argv) - 1

i = 0
result = 0
for arg_vector in sys.argv:
    if i != 0:
        result += int(arg_vector)
    else:
        i += 1
print("{:d}".format(result))
