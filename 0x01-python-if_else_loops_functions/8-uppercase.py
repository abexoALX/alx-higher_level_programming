#!/usr/bin/python3
def uppercase(str):
    temp = ""
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            temp = temp + chr(ord(str[i]) - 32)
        else:
            temp = temp + str[i]
    print("{}".format(temp))
