#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    count_a = len(tuple_a)
    count_b = len(tuple_b)
    new_tuple = ()

    for i in range(2):
        if i >= count_a:
            tup_a = 0
        else:
            tup_a = tuple_a[i]
        if i >= count_b:
            tup_b = 0
        else:
            tup_b = tuple_b[i]

        if (i == 0):
            new_tuple = (tup_a + tup_b)
        else:
            new_tuple = (new_tuple, tup_a + tup_b)

    return (new_tuple)
