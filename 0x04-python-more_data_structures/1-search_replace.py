#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    count = len(new_list)

    for i in range(count):
        if new_list[i] == search:
            new_list.pop(i)
            new_list.insert(i, replace)

    return new_list
