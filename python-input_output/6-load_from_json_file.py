#!/usr/bin/python3
"""module with function with load_from_json_file
function that converts json to object"""

import json

def load_from_json_file(filename):
    '''filename where we have to extract the json string
    to convert to object'''

    with open(filename, mode="r+", encoding="utf-8")as f:
        read_file=f.read()
        return json.loads(read_file) 
