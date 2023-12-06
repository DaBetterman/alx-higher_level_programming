#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    count = 0

    for i in my_list:
        if i not in new_list:
            count += i
            new_list.append(i)
    return (count)
