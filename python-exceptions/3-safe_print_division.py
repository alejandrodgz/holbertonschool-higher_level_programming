#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    except:
        return None
    finally:
        if b == 0:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {}".format(a / b))
    return c

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))