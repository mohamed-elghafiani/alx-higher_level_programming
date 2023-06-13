#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for el in line[:-1]:
            print("{:d}".format(el), end=" ")
        print(line[1])
