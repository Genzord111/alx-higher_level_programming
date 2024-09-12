#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        result = 0
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        operator = sys.argv[2]

        if operator == '+':
            result = add(a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, result))
            sys.exit(0)
        elif operator == '-':
            result = sub(a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, result))
            sys.exit(0)
        elif operator == '/':
            result = div(a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, result))
            sys.exit(0)
        elif operator == '*':
            result = mul(a, b)
            print("{} {} {} = {}".format(a, sys.argv[2], b, result))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
