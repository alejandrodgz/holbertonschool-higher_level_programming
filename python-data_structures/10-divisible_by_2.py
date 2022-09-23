#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list2 = []
    a = 0
    for i in my_list:
        if my_list[a] % 2 == 0:
            list2.append(True)
        else:
            list2.append(False)
        a += 1
    print(list2)

    return list2
