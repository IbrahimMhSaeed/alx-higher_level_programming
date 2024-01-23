#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    for r, row in enumerate(matrix):
        for i, c in enumerate(row):
            if i != (len(row) - 1) and c != '-':
                print("{:d}".format(c), end=' ')
            else:
                print("{:d}".format(c))
