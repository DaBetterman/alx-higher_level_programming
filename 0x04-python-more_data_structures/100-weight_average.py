#!/usr/bin/python3
def weight_average(my_list=[]):
    count = len(my_list)
    if count == 0:
        return (0)
    average = [ave * weight for (ave, weight) in my_list]
    return sum(average) / sum([weight for (ave, weight) in my_list])
