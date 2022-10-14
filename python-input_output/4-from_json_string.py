#!/usr/bin/python3
'''this module has the function
from_json_string Write a function 
that returns an object '''
import json

def from_json_string(my_str):
    '''my_str is the string to convert
    to a phyton object'''

    return json.loads(my_str)
