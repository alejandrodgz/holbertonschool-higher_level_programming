#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if isinstance(roman_string, str) is False:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 50}
    a = 0
    for i in range(len(roman_string) - 1):
        if dic[roman_string[i]] < dic[roman_string[i + 1]]:
            a = a - dic[roman_string[i]]
        else:
            a = a + dic[roman_string[i]]
    a = a + dic[roman_string[len(roman_string) - 1]]
    return a
