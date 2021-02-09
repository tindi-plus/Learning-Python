# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 20:00:03 2021
Reimplementing DataFrame's output
@author: Tindi.Sommers
"""


def format_dic(dic):
    """A function for formatting a DataFrame's output in a table format"""

    # a list for keeping the field width of all the columns
    fw = []

    for key, values in dic.items():
        a = len(key)  # get the length of the key
        v = [f'{x}' for x in values]  # convert values to strings
        lengths = [len(x) for x in v]  # create a list of the length of the strings
        lengths.append(a)  # add the length of key to the list of lengths
        fw.append(max(lengths))

    # print the column headers
    print('   ', end='')
    for index, i in enumerate(dic.keys()):
        print(f'{i:<{fw[index]}}', end=' ')
        # print(index)
    print()

    # print the rest of the table
    for i in range(len(max(dic.values()))):
        print(f'{i}  ', end='')
        for v in dic.values():
            print(f'{v[i]:>{fw[i]}}', end=' ')
        print()


a = {'Eva': [2, 5, 6], 'John': [77, 3, 1], 'Joy': [22, 3, 60],
     'Joe': [33, 681, 77]}
format_dic(a)




