#!/usr/bin/python3

"""this module is containing a read_file functoin"""


def read_file(filename=""):
    """this function is to read the date in a file and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        r = f.read()
        print(r, end="")
