#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    idx = idx + 1
    if idx < 1:
        return my_list
    
    elif idx > len(my_list):
        return my_list
    idx = idx -1
    my_list.pop(idx)
    
    my_list.insert(idx, element)

    return (my_list)
