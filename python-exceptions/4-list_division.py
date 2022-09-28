#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    listend = [0 for x in range(list_length)]
    for i in range(list_length):
        try:
            listend[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            listend[i] = 0
            print("division by 0")
        except TypeError:
            listend[i] = 0
            print("wrong type")
        except IndexError:
            listend[i] = 0
            print("out of range")
    return (listend)
