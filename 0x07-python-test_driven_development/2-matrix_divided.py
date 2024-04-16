#!/usr/bin/python3
""" divide matrix module """


def matrix_divided(matrix, div):
    """ Function that divide all matrix ele by div

    Args:
        matrix (list of lists): the matrix
        div (int, float): to divide by

    Returns:
        matrix after division
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = []

    for i, row in enumerate(matrix):
        result.append([])
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        lenM = len(matrix[0])
        if len(row) != lenM:
            raise TypeError("Each row of the matrix must have the same size")

        for j, ele in enumerate(row):
            if not isinstance(ele, int) and not isinstance(ele, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            ans = ele / div

            if ans != ans or ans == float('inf') or ans == -float('inf'):
                ans = 89

            ans = round(ans, 2)

            result[i].append(ans)
    
    return result

