#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == '+':
        print("{} + {} = {}".format(sys.argv[1],
                                    sys.argv[3],
                                    cal.add(int(sys.argv[1]),
                                            int(sys.argv[3]))))
    if sys.argv[2] == '-':
        print("{} - {} = {}".format(sys.argv[1],
                                    sys.argv[3],
                                    cal.sub(int(sys.argv[1]),
                                            int(sys.argv[3]))))
    if sys.argv[2] == '*':
        print("{} * {} = {}".format(sys.argv[1],
                                    sys.argv[3],
                                    cal.mul(int(sys.argv[1]),
                                            int(sys.argv[3]))))
    if sys.argv[2] == '/':
        print("{} * {} = {}".format(sys.argv[1],
                                    sys.argv[3],
                                    cal.div(int(sys.argv[1]),
                                            int(sys.argv[3]))))
    if sys.argv[2] != '+' and sys.argv[2] != '-' and sys.argv[2] != '*' and sys.argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
