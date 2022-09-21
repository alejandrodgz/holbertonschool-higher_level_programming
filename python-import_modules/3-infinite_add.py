#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    b = 0
    for i in sys.argv[1:]:
        b = b + int(i)
    print(b)
