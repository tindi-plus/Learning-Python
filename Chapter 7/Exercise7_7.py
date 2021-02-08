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

    # convert the ndarray into a one dimensional list
    oda = []
    for i in array:
        for j in i:
            oda.append(j)

    # get the element with the largest field with
    fw = np.max(oda)

    # format each element in the array
    for a in range(len(array)):
        for b in range(len(array[a])):
            array[a][b] = f'{array[a][b]:<{fw}}'

    print(array)


a = [[1, 2.2, 3, 4, 5.05], [5.9, 2, 12, 234, 4]]

format_ndarray(a)