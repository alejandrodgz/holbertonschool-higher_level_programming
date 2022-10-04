#!/usr/bin/python3
''' module 2-matrix_divided - divided every
element in a matrix with integers or float
div must be different from 0
'''


def matrix_divided(matrix, div):
    '''matrix is a matrix with same length in its rows
    div must be different from 0
    matrix elements must be int or float type'''

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    b = len(matrix[0])
    for a in matrix:
        if len(a) != b:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[0 for k in range(len(matrix[0]))]
                  for l in range(len(matrix))]
    y = 0
    error1 = "matrix must be a matrix (list of lists) of integers/floats"
    for i in matrix:
        z = 0
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(error1)
            else:
                new_matrix[y][z] = round(float(j / div), 2)
                z += 1
        y += 1
    return new_matrix
