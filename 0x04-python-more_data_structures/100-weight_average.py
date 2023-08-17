#!/usr/bin/python3

def weight_average(my_list=[]):

    if len(my_list) == 0:
        return 0

    suma = sumb = product = ave = 0
    for tup in my_list:
        suma += tup[1]
        product = tup[0] * tup[1]
        sumb += product
        ave = sumb / suma
    return ave
