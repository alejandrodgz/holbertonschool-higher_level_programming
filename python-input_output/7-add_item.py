#!/usr/bin/python3
'''module with add_item function
that Writes a script that adds all arguments to a
Python list'''

import sys
import os.path
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
if os.path.exists('add_item.json') is True:
    file_list = load_from_json_file('add_item.json')
    if len(sys.argv) == 1:
        save_to_json_file(file_list, 'add_item.json')
    else:
        for i in sys.argv[1:]:
            file_list.append(i)
        save_to_json_file(file_list, 'add_item.json')
else:
    with open('add_item.json', mode='w+', encoding='utf-8') as f:
        if len(sys.argv) == 1:
            list2 = []
            save_to_json_file(list2, 'add_item.json')
        else:
            list2 = []
            for i in sys.argv[1:]:
                list2.append(i)
            save_to_json_file(list2, 'add_item.json')
