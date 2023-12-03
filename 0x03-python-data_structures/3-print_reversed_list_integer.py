#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    count = len(my_list)
    reverse_list = (my_list)[::-1]
    for i in range(count):
        print("{:d}".format(reverse_list[i]))
