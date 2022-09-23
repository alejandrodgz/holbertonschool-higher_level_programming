#!/usr/bin/python3
from operator import add


def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if a > 0:
        add_a = tuple_a[0]
    else:
        add_a = 0
    if a > 1:
        add_a2 = tuple_a[1]
    else:
        add_a2 = 0
    if b > 0:
        add_b = tuple_b[0]
    else:
        add_b = 0
    if b > 1:
        add_b2 = tuple_b[1]
    else:
        add_b2 = 0

    tuple_c = ((add_a + add_b), (add_a2 + add_b2))
    return tuple_c
