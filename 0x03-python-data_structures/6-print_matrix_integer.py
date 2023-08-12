#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for list_ in matrix:
        for i in range(len(list_)):
            if i == len(list_) - 1:
                print("{:d}".format(list_[i]))
            else:
                print("{:d}".format(list_[i]), end=" ")
