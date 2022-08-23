#!/usr/bin/python3
def remove_char_at(str, n):
    temp = ""
    if (n < 0):
        return str
    else:
        for i in range(len(str)):
            if (i != n):
                temp = temp + str[i]
    return temp
