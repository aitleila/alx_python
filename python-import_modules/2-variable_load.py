#!/usr/bin/python3

import variable_load_2

def main():
    global a
    a = 98

    result = a
    print("{} = {}".format(a, result))

if __name__ == "__main__":
    main()
