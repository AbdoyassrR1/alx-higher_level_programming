#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        i = 0   
        my_list.reverse()
        for num in my_list: 
            print("{:d}".format(my_list[i]))
            i += 1
