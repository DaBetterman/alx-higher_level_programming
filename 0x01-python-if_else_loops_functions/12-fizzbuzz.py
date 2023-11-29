#!/usr/bin/python3
def fizzbuzz():
        j = 1
        k = 1
        for i in range(1, 101):
            if i == (3 * j) and i == (5 * k):
                print("FizzBuzz", end=" ")
                k = k + 1
                j = j + 1
            elif i == (3 * j):
                  print("Fizz", end=" ")
                  j = j + 1
            elif i == (5 * k):
                  print("Buzz", end=" ")
                  k = k + 1
            else:  
                print("{}".format(i), end=" ")
