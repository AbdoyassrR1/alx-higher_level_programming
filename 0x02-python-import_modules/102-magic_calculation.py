#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        res = add(a, b)
        for i in range(4, 6):
            res = add(res, i)
        return (res)

    else:
        return(sub(a, b))
