#!/usr/bin/python3
def max_integer(my_list=[]):
    count_list = len(my_list)
    if count_list == 0:
        my_list = None
        return (my_list)

    my_list.sort()
    return (my_list[-1])
