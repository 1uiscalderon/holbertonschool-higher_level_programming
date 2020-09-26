#!/usr/bin/python3
"""Module that contains a simple function to divides all elements of a matrix.
This module must be imported to be used.
    -To run doctests:
        $ python3 -m doctest -v ./tests/2-matrix_divided.txt
"""


def matrix_divided(matrix, div):
    """Divides a matrix by a Number
    Args:
        matrix: Matrix with list of list.
        div: Number to divide each element of the matrix.
    Returns:
        New matrix with the result
    Raises:
        -TypeError: If the elements of the matrix arent int
        or float, or arent a list.
        -ZeroDivisionError: If div is 0.
"""
    if type(matrix) is not list or len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(matrix[0]) != len(i):
            raise TypeError("Each row of the matrix must have the same size")

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    return [[round(j / div, 2) for j in i] for i in matrix]
