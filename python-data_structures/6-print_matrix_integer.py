#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        a = len(matrix)
        b = len(matrix[0])
        j = 0
        i = 0   

        while i < a:
            j = 0
            while j < b:
                if j == b - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
                j += 1
            i += 1
    else:
        print("s")
        return
