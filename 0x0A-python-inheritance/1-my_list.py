#!/usr/bin/python3

"""this module containing a class named mylist that inherits form list class"""


class MyList(list):

    """ inherits form list class """

    def print_sorted(self):
        """"functoin to print a sorted list"""
        newlist = sorted(self)
        print(newlist)
