# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 12:40:41 2021.

a frozen complex class

@author: Tindi.Sommers
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Complex:
    """Complex class that represents a complex number 
    with real and imaginary parts."""

    real: int
    imaginary: int

    def __add__(self, right):
        """Overrides the + operator."""
        return Complex(self.real + right.real, 
                       self.imaginary + right.imaginary)

    def __iadd__(self, right):
        """Overrides the += operator."""
        self.real += right.real
        self.imaginary += right.imaginary
        return self

    def __repr__(self):
        """Return string representation for repr()."""
        return (f'({self.real}' + 
                (' + ' if self.imaginary >= 0 else ' - ') +
                f'{abs(self.imaginary)}i)')