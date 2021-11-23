#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(len(matrix)):
        for idxTwo in range(len(matrix[idx])):
            print("{:d}".format(matrix[idx][idxTwo]), end="")
            if idxTwo != (len(matrix[idx]) - 1):
                print(" ", end="")

        print("")
