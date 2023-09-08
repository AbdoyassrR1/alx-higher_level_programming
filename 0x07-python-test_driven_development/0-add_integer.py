#!/usr/bin/python3

"""
this is 0-add_integer module
it contain a function to adding two numbers
"""


def add_integer(a, b=98):
    """
    Args: a,b float or integers
    Return: sum of a and b
    """
    if type(a) is not int or type(b) is not int:

        if type(a) is float or type(b) is float:
            a = int(a)
            b = int(b)

        else:

            raise TypeError("a must be an integer or b must be an integer")
    return a + b
