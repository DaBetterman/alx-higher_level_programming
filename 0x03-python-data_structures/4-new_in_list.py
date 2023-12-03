#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = list(my_list)
    idx = idx + 1

    if idx < 1:
        return my_list
    elif idx > len(my_list):
        return my_list

    idx = idx - 1

    new_list.pop(idx)

    new_list.insert(idx, element)

    return (new_list)
