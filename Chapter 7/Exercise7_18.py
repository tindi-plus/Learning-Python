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
    array_sorted = np.sort(array)


