# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:25:37 2021.

Modifying account class

@author: Tindi.Sommers
"""

"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self._name = name
        self._balance = balance
    
    @property
    def name(self):
        return self._name
    
    @property
    def balance(self):
        return self._balance
    
    
    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self._balance += amount