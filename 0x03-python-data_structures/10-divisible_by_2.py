#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    index = 0
    for i in my_list:
        if i % 2 == 0:
            new_list[index] = True
        else:
            new_list[index] = False
        index = index + 1
    return new_list

