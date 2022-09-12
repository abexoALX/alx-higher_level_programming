#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for index in range(x):
        try:
            print(my_list[index], end='')
            num += 1
        except Exception as error:
            break
    print('')
    return num
