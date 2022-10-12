#!/usr/bin/python3
"""
Module 1-my_list+

Contains class MyList
inherits from list; has public instance method to print sorted
"""

class Mylist(list):
    """inherits from list
    
    methods:
    print_sorted(self)
    """

    def print_sorted(self):
        '''method to print every
        element of self list sorted'''
        a = self[:]
        new_list = sorted(a)
        print(new_list)
