#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    dirs = dir(hidden_4)
    for el in dirs:
        if el[:2] != "__":
            print("{}".format(el))
