# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 21:39:10 2021.

Class Account for banking purposes

@author: Tindi.Sommers
"""
"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance = Decimal('0.00')):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount
    
    def withdraw(self, amount):
        """withdraw money from the bank account"""
        
        # if the withdrawal amount is less than zero, raise ValueError
        if amount < Decimal('0.00'):
            raise ValueError('Amount cannot be less than zero.')
        if amount > self.balance:
            raise ValueError('Insufficient balance')
        
        self.balance -= amount
            

class SavingsAccount(Account):
    """Account for keeping a savings bank account balance."""
    
    def __init__(self, name, balance, rate):
        """Initialize the properties of the class"""
        
        # call the constructor of the base class to initialize its properties
        super().__init__(name, balance)
        
        # create property rate for the class
        self.interest_rate = rate
    
    @property
    def interest_rate(self):
        return self._interest_rate
    
    @interest_rate.setter
    def interest_rate(self, rate):
        """Set the interest rate of the savings account"""
        self._interest_rate = rate
    
    def calculate_interest(self):
        """calculate the interest earned by the savings account"""
        return self.balance * self.interest_rate


class CheckingAccount(Account):
    """Account for a checking account balance"""
    
    def __init__(self, name, balance, fee = Decimal('0.00')):
        """Initialize the Checking account"""
        
        # initialize the base class Account cosntructor
        super().__init__(name, balance)
        
        self.fee = fee

    @property
    def fee(self):
        """get the fee for the checking account"""
        return self._fee
    
    @fee.setter
    def fee(self, amount):
        """set the fee for the checking account"""
        if amount < Decimal('0.00'):
            raise ValueError('fee must be >= 0.00')
            
        self._fee = amount
    
    def deposit(self, amount):
        """deposit money into the account"""
        
        # call on the base class method deposit to deposit 
        # an amount with the fee deducted
        super().deposit(amount - self.fee)
    
    def withdraw(self, amount):
        """withdraw money from the account"""
        
        # call on the base class method withdraw to withdraw the amount + fee
        super().withdraw(amount + self.fee)
        

    

    
    
    
                