#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):

    if not my_list:
        return

    rev_list = my_list[::-1]

    for item in rev_list:
        print("{:d}".format(item))
