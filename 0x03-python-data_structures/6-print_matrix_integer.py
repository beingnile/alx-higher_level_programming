#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    for row in matrix:
        for elem in row:
            if elem == row[-1]:
                print("{:d}".format(elem))
                break
            print("{:d}".format(elem), end=" ")
