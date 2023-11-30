#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argv = sys.argv
    arg_count = len(argv) - 1

    if arg_count != 3:
        sys.stdout.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    operator = argv[2]
    if operator not in ['+', '-', '*', '/']:
        sys.stdout.write("Unknown operator. \
Available operators: +, -, * and /\n")
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)

    sys.stdout.write(f"{a} {operator} {b} = {result}\n")
