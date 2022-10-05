#!/usr/bin/python3
'''this module has one function named print_square
the functions prints and square of size (size)
just that'''


def print_square(size):
    '''size is the size in '#' caracters
    no more arguments'''

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    a = 0
    while a < size:
        b = 0
        while b < size:
            print('#', end="")
            b += 1
        print("")
        a += 1
