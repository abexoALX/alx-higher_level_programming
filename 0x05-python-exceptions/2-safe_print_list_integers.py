#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for index in range(x):
        try:
            print('{:d}'.format(my_list[index]), end='')
            val += 1
        except IndexError:
            break
        except TypeError:
            pass
    print('')
    return val
