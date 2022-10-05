#!/usr/bin/python3
'''this is 3-say_my_name module with one
function, say_my_name, that...writes your name
funny hah'''

def say_my_name(first_name, last_name=""):
    '''first_name must be a string
    last_name must be a string'''
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
