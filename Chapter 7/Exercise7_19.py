# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:57:04 2021
median and mode for Numpy
@author: Tindi.Sommers
"""

import numpy as np


def one_D_median(array):
    """
    Determine the median of an array.

    Parameters
    ----------
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    the median of the given array.

    """
    # sort the array in ascending order
    array_sorted = np.sort(array, axis=None)

    length = len(array_sorted)

    if length % 2 == 1:
        array_median = array_sorted[length // 2]
    else:
        array_median = (array_sorted[length // 2] + array_sorted[(length // 2) - 1]) / 2
    return array_median


def median(array, axis=None):
    """
    Determine the median of an array.

    Parameters
    ----------
    array : TYPE
        DESCRIPTION.

    Returns
    -------
    the median of the given array.

    """
    if axis is None:
        return one_D_median(array)
    elif axis == 0:
        median_array = np.array([])
        # split the array into equal rows and then call on
        # one_D_median to find the median of each row.
        for i in np.split(array, len(array)):
            median_array = np.concatenate((median_array, one_D_median(i)), axis=None)
        return median_array
    elif axis == 1:
        median_array = np.array([])
        # transpose the array and split it into equal rows and then call on
        # one_D_median to find the median of each row.
        for i in np.split(array.T, len(array.T)):
            median_array = np.concatenate((median_array, one_D_median(i)), axis=None)
        return median_array


test = np.random.randint(0, 4, 15).reshape(3, 5)
print(test)

print(median(test, axis=1))

