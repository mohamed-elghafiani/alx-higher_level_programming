#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv
    ln = len(args)
    if ln <= 1:
        print("0 arguments.")
    else:
        msg = "argument" if ln == 2 else "arguments"
        print("{} {}:".format(ln - 1, msg))
        for idx, el in enumerate(args[1:]):
            print("{}: {}".format(idx + 1, el))
