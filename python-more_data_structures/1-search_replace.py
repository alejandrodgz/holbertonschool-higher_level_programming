#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            my_list2[i] = replace
    return my_list2
