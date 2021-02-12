# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:25:52 2021.

Median and Mode for Numpy
@author: Tindi.Sommers
"""

import numpy as np


def median(array):
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



test = np.random.randint(0, 4, 10).reshape(2, 5)
print(test)

print(median(test))


