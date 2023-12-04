#!/usr/bin/python3
def max_integer(my_list=[]):
    count_list = len(my_list)
    if count_list == 0:
        my_list = None
    max_num = 0
    for i in range(count_list):
        if my_list[i] > max_num:
            max_num = my_list[i]
        else:
            pass
    return (max_num)
