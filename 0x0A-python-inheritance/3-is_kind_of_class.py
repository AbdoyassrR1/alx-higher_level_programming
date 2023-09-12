#!/usr/bin/python3
"""
This module provides a function to check whether an object
is an instance of a specified class or a subclass thereof.
"""


def is_kind_of_class(obj, a_class):
    """
    Check whether the given object is an instance of the specified
    class or a subclass thereof.
    """

    return isinstance(obj, a_class)
