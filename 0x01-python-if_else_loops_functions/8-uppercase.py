#!/usr/bin/python3
def uppercase(str):
    upper = ""

    for char in str:
        if ord(char) in range(97, 123):
            chars_in_upper = ord(char) - 32
            upper += chr(chars_in_upper)
        else:
            upper += char

    print("{}".format(upper))
