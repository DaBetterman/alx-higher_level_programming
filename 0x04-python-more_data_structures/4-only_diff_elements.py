#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set_1 = set_1 - set_2
    new_set_2 = set_2 - set_1
    combo_set = new_set_1 | new_set_2
    return (combo_set)
