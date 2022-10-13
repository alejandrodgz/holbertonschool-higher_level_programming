#!/usr/bin/python3
'''this module has the write_file function
and is about writing a string to a file
or created if does not exist'''


def write_file(filename="", text=""):
    """text, string
    filename, file to write or create"""

    with open(filename, mode="w+", encoding="utf-8")as f:
        return f.write(text)
