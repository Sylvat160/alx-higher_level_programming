#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    # matrix = [[row[i] for i in range(len(row))] for row in matrix]
    transposed = []
    for i in range(len(matrix)):
        transposed.append([row[i] for row in matrix])
    print("{}".format(transposed))
