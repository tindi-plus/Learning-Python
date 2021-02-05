# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:35:03 2021
Testing if a sequence is sorted
@author: Tindi.Sommers
"""
# function for testing a sequence if it is sorted


def sort_test(arg):
    # ensure the input is a list
    my_List = []
    my_List += arg
    if my_List == sorted(my_List):
        print(f'The sequence {arg} is sorted.')
    else:
        print(f'The sequence {arg} is not sorted.')


sort_test((8, 7, 8, 9))
