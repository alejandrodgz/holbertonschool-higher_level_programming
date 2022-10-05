#!/usr/bin/python3
'''this the 5-text_indentation module with one function
called text_indentation, the function creates a new line
when these characteres are found (. , ? :)'''


def text_indentation(text):
    ''' text is a string
    where we will indent every
    character of the ones mentioned in
    the module description'''


    if isinstance(text, str) is False:
        raise TypeError('text must be a string')
    a = 0
    for i in range(len(text)):
        if (text[i] == '.') or (text[i] == '?' or text[i] == ':'):
            new_string = text[a:i + 1]
            print(new_string)
            print("")
            a = i + 1
            k = a
            while k <= len(text) - 1 and text[k] == " ":
                i += 1
                a += 1
                k += 1

    new_string = text[a:i + 1]
    print(new_string, end="")
