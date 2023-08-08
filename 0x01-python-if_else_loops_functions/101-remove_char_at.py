#!/usr/bin/python3
def remove_char_at(str, n):
    res = ""
    i = 0
    for char in range(len(str)):
        if i == n:
            i += 1
            continue
        else:
            res += str[i]
            i += 1
    return res
