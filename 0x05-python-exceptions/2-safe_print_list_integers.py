#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            else:
                pass
        print("")
        return (count)
    except ValueError:
        print("")
        return (count)
