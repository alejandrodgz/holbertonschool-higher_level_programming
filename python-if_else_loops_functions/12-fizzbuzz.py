#!/usr/bin/python3
def fizzbuzz():
        i = 1
        while i < 101:
                if i % 3 == 0 and i % 5 == 0:
                        print("{}".format("FizzBuzz"), end=" ")
                        i += 1
                elif i % 5 == 0:
                        print("{}".format("Buzz"), end=" ")
                        i += 1
                elif i % 3 == 0:
                        print("{}".format("Fizz"), end=" ")
                        i += 1
                else:
                        print("{}".format(i), end=" ")
                        i += 1
