#!/usr/bin/python3
'''module with to_json_string function
returns the json represantation of an object'''

import json


def to_json_string(my_obj):
    '''my_obj is the object
    to convert in json representation'''

    return json.dumps(my_obj)
