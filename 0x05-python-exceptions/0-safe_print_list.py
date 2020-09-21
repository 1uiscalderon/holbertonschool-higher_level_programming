#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    result = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            break
        else:
            result += 1
    print()
    return result
