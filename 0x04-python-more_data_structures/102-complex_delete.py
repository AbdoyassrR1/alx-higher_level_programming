#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    new_dict = a_dictionary.copy()
    for ke, val in new_dict.items():
        if val == value:
            del a_dictionary[ke]
    return a_dictionary
