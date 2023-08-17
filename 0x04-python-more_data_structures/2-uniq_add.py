#!/usr/bin/python3

def uniq_add(my_list=[]):

    for num in my_list:
        count_ = my_list.count(num)
        if count_ > 1:
            for i in range(count_ - 1):
                my_list.remove(num)

    return sum(my_list)
