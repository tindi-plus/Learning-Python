# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 22:03:50 2021

@author: Tindi.Sommers
"""

import doctest
def maximum(value1, value2, value3):
    """Return the maximum of three values.
    >>> maximum(22, 4, 7)
    22
    
    >>> maximum(1.4, 5.7, 1.9)
    5.7
    
    >>> maximum('F', 'N', 'e')
    'e'
    
    """
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

if __name__ == '__main__':
    doctest.testmod(verbose=True)

import dataclasses
from decimal import Decimal
Account = dataclasses.make_dataclass('Account', [('account', int),
                                                 ('name', str),
                                                 ('balance', Decimal)])
myAcct = Account(254637, 'Thomas', Decimal('5000'))
print(myAcct)
