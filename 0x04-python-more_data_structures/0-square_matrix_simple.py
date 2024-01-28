#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    sqr = []
    for mat in matrix:
        sqr.append(list(map(lambda x: x**2, mat)))
    return (sqr)
