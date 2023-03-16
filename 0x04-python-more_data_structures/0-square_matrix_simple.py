#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        squares = []
        for element in row:
            squares.append(element ** 2)
        new.append(squares)

    return new
