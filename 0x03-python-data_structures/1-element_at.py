#!/usr/bin/python3
def element_at(my_list, idx):
    idx = idx + 1
    if idx < 1:
        return None
    elif idx > len(my_list):
        return None
    return (idx)
