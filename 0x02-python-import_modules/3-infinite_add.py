#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv

    sum_ = 0
    for el in args[1:]:
        sum_ += int(el)

    print("{}".format(sum_))
