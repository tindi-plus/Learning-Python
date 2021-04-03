# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:07:51 2021.

Class Invoice for materials at a store

@author: Tindi.Sommers
"""

from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Invoice:
    """Attributes of class invoice"""
    part_number: str
    part_description: str
    quantity: int
    price: Decimal
    
    @property
    def quantity(self):
        """Get the quantity of materials"""
        return self._quantity
    
    @quantity.setter
    def quantity(self, number):
        """verify that the quantity is not negative"""
        if number < 0:
            raise ValueError('The quantity cannot be less than zero.')
        self._quantity = number
    
    @property
    def price(self):
        """Get the price per item"""
        return self._price
    
    @price.setter
    def price(self, amount):
        """set the price per item. Must not be negative"""
        if amount < Decimal('0'):
            raise ValueError('The price per item cannot be less than zero.')
        self._price = amount
    
    def calculate_invoice(self):
        """Get the invoice for items sold"""
        money = self.quantity * self.price
        return f'Invoice is NGN{money}'
    
        