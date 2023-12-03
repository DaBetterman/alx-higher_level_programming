#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for number in matrix:
        for i in range(len(number)):
            print("{:d}".format(number[i]), end="")
            if i != len(number) - 1:
                print(" ", end="")
        print()
