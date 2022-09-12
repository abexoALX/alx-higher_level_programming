#!/usr/bin/python3
def safe_print_integer(value):
    val = True
    try:
        print('{:d}'.format(value))
    except Exception as error:
        val = False
    return val
