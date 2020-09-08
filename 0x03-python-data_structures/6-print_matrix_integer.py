#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        cont = 0
        for j in i:
            cont += 1
            if len(i) != cont:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print()
