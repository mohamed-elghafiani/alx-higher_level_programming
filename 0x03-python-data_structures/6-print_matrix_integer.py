#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        ln = len(line)
        for i in range(ln):
            if i == ln - 1:
                print("{:d}".format(line[i]), end="")
                break
            print("{:d}".format(line[i]), end=" ")
        print("")
