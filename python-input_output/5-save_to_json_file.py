#!/usr/bin/python3
'''this module is all about to make a
function that writes an Object to a text file'''
import json


def save_to_json_file(my_obj, filename):
    '''filename and objetc to write in json represantion'''

    with open(filename, mode="w+", encoding="utf-8")as f:
        return f.write(json.dumps(my_obj))
