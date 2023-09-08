#!/usr/bin/python3

"""
    This module contains the definitions of the function `matrix_divided()`
    that divides all elements of a matrix
"""


def matrix_divided(matrix=[[0]], div=1):
    """ matrix_divided divides all elements of a matrix by div

    Args:
      matrix: A matrix composed of a list of lists of integers/floats
      div: A number float/integer != 0

    Raises:
      TypeError: if div is not a number or matrix is not a list of lists of
                numbers where each row have the same size
      ZeroDivisionError: if div == 0
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not all(isinstance(item, list) for item in matrix):
        msg = "matrix must be a matrix (list of lists) of integers/floats"
        raise TypeError(msg)
    row_0_size = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if len(row) != row_0_size:
            raise TypeError("Each row of the matrix must have the same size")
        row_is_int = all(isinstance(el, int) for el in row)
        row_is_float = all(isinstance(el, float) for el in row)
        if not row_is_int and not row_is_float:
            msg = "matrix must be a matrix (list of lists) of integers/floats"
            raise TypeError(msg)
        new_row = [round(el/div, 2) for el in row]
        new_matrix.append(new_row)

    return new_matrix
