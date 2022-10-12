#!/usr/bin/python3
'''
documentation for module my_list
contain class Mylist 
working
'''

class Mylist(list):
    '''list of int type that
    inherits from list
    
    methods:
    print_sorted(self)
    '''

    pass

    def print_sorted(self):
        '''method to print every
        element of self list sorted'''
        a = self[:]
        new_list = sorted(a)
        print(new_list)
