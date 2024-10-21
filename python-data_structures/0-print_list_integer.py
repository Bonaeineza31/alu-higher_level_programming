#!/usr/bin/python3
def print_list_integer(my_list=[]):
    return '\n'.join("{:d}".format(item) for item in my_list)

