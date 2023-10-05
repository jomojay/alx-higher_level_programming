#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    a = len(argv)
    if a == 1:
        print("{:d} arguments.".format(a - 1))
    else:
        j = 1
        if a == 2:
            print("{:d} argument:".format(a - 1))
        else:
            print("{:d} arguments:".format(a - 1))
        for i in argv:
            if i is not argv[0]:
                print("{:d}: {:s}".format(j, i))
                j += 1
