#!/usr/bin/python3

def no_c(my_string):

    count_c = my_string.count("c")
    count_C = my_string.count("C")

    i = 0
    while count_c > 0:

        while i < len(my_string):

            if my_string[i] == 'c':

                my_string = my_string[:i] + my_string[i + 1:]
                count_c -= 1
                if count_c != 0:
                    i = -1

            i += 1
    i = 0
    while count_C > 0:

        while i < len(my_string):

            if my_string[i] == 'C':

                my_string = my_string[:i] + my_string[i + 1:]
                count_C -= 1
                if count_C != 0:
                    i = -1

            i += 1

    return my_string
