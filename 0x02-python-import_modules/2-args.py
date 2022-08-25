#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    if total <= 1:
        print("0 arguments.")
    else:
        print("{:d} argument:".format(total - 1))
        for i in range(1, total):
            print("{:d}: {}".format(i, sys.argv[i]))
