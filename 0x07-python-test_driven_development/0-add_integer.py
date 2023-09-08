#!/usr/bin/python3
"""
This is the 0-add_integer module.
"""


def add_integer(a, b=98):
    """
       Return an integer: sum of 2 numbers
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, int):
        raise TypeError("b must be an integer or float")
    return a + b
