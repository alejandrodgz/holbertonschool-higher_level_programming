#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        tuple3 = (0, "None")
        return tuple3
    tuple1 = (len(sentence), sentence[0])
    return tuple1
