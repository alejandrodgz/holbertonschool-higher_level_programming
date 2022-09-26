#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = {}
    a = sorted(a_dictionary)
    for i in a:
        s[i] = a_dictionary[i]
    for j, k in s.items():
        print(f"{j}: {k}")
