# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:50:54 2021
Implementing Numpy array formatted output
@author: Tindi.Sommers
"""
import numpy as np


def format_ndarray(array):
    """A function for formatting a multidimensional array such that it
    is displayed in neat columns with each eledment right alingned with
    a field with of the element with the largest character field."""

    # convert the ndarray into a one dimensional list and save as strings
    oda = []
    for i in array:
        for j in i:
            oda.append(f'{j}')

    # get the element with the largest field width
    fw = np.max([len(x) for x in oda])

    # format each element in the array
    for a in range(len(array)):
        for b in range(len(array[a])):
            array[a][b] = f'{array[a][b]:<{fw}}'

    for i in array:
        print(i)


a = [[1, 2.2, 3, 4, 5.05], [5.9, 2000, 12, 234, 4], [12, 647, 23, 90, 22]]

format_ndarray(a)
