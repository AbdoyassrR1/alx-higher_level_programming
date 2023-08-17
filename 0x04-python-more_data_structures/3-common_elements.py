#!/usr/bin/python3

def common_elements(set_1, set_2):
    comm = []
    for item in set_1:
        if item in set_2:
            i = 0
            comm.append(item)
            i += 1
    return set(comm)
