#!/usr/bin/python3
""" This module is about a function to divide matrix elements"""


def matrix_divided(matrix, div):
    """
      function that divides all elements of a matrix
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix:
        raise TypeError(error_msg)
    if not isinstance(matrix, list):
        raise TypeError(error_msg)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(error_msg)

    for num in row:
        if len(row) == 0:
            raise TypeError(error_msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
