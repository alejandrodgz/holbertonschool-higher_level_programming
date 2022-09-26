#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            matrix2[i][j] = matrix[i][j] ** 2
    return matrix2
