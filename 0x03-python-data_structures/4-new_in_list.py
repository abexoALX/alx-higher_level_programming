#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return
    new_list = my_list.copy()
    if idx >=0 and idx < len(new_list):
        new_list[idx] = element
    return new_list
