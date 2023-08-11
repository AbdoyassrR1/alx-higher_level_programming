#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    i = 1
    args = sys.argv
    len_of_args = len(args) - 1

    if len_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    elif len_of_args == 3:
        if args[2] == "+":
            print("{} + {} = {}".format(args[1], args[3],
                                        int(args[1]) + int(args[3])))

        elif args[2] == "-":
            print("{} + {} = {}".format(args[1], args[3],
                                        int(args[1]) - int(args[3])))

        elif args[2] == "*":
            print("{} + {} = {}".format(args[1], args[3],
                                        int(args[1]) * int(args[3])))

        elif args[2] == "/":
            print("{} + {} = {}".format(args[1], args[3],
                                        int(args[1]) / int(args[3])))

        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
