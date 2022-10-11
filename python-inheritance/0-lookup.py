#!/usr/bin/python3
"""module with lookup function
returns avalaible atributtes and methods
in a object
"""

def lookup(obj):
    """function with one 
    parameter"""
    a = dir(obj)
    return a    
