#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arguments = len(argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(arguments))
    if arguments >= 1:
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))
