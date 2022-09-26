#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    s = {}
    for a, b in a_dictionary.items():
        s[a] = a_dictionary[a] * 2
    return s
