#!/usr/bin/python3
"""
 A function that divides all elements of a matrix.
"""
def matrix_divided(matrix, div):
    """
    Validating the matrix
    """
    for row in matrix:
        if not isinstance(row, list) or len(row) != len(matrix[0]):
            raise TypeError("matrix must be a matrix (list of lists) with the same size in each row")
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """
    Validating the div
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """
    Validating the div if it is zero
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """
    Divide all elements of the matrix by div, rounded to 2 decimal places
    """
    new_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return new_matrix
