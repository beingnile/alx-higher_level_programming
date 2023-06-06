#!/usr/bin/python3
"""Defines a function for matrix division"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix with div

    Args:
        matrix(list): A list of lists with integers
        or floats to be divided

        div(int): The function will divide the elements by div

    Returns: A new matrix with the results
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(matrix_err)
    if len(matrix) == 0:
        raise TypeError(matrix_err)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_err)
        if len(row) == 0:
            raise TypeError(matrix_err)
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(matrix_err)

    # Check for matrix size
    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check for div validity
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    num_rows = len(matrix)
    num_cols= len(matrix[0])
    res = [[0 for j in range(num_cols)] for i in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            result = round(matrix[i][j] / div, 2)
            res[i][j] = result

    return res
