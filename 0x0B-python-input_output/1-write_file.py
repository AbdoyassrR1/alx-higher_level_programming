#!/usr/bin/python3

"""
writes a string to a text file (UTF8) and
returns the number of characters"""
def write_file(filename="", text=""):



    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    with open(filename, "r", encoding="utf-8") as f:
        r = f.read()
        c = len(r)
        return c
