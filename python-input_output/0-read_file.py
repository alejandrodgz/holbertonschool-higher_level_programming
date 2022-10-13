#!/usr/bin/python3
"""this module has a function to read
a file called read_file"""

def read_file(filename=""):
    """filename is the name of
    the file to read and print"""

    with open(filename, mode="r", encoding="utf-8")as f:
        file_read=f.read()
        for line in file_read:
            print(line,end="")
