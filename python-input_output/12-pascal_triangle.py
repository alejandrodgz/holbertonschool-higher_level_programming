#!/usr/bin/python3
'''the pascal triangle'''


def pascal_triangle(n):
    '''function triangle'''
    if n <= 0:
        list2 = []
        return list2
    list1 = [[] for j in range(n)]

    for i in range(n):
        j = 0
        while j <= i:
            if (i - 1 >= 0 and j > 0) and (j < i):
                k = list1[i - 1][j - 1] + list1[i - 1][j]
                list1[i].append(k)
            else:
                k = 1
                list1[i].append(k)
            j += 1
    return list1
