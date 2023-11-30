#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

arg_vector = "{:d} argument"
arg_count = len(sys.argv) - 1
if arg_count == 0:
    arg_vector += 's.'
elif arg_count == 1:
    arg_vector += ':'
else:
    arg_vector += 's:'
print(arg_vector.format(arg_count))

num = 0
for i in sys.argv:
    if num != 0:
        print("{:d}: {:s}".format(num, i))
    num += 1
