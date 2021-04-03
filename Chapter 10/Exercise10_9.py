# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:49:33 2021.

Creating a square shape as a dataclass

@author: Tindi.Sommers
"""

from dataclasses import dataclass
import math

@dataclass
class Square:
    
    side: int  # a side of the square
    
    def area(self):
        """Calculate and return the area of the square"""
        return self.side ** 2
    
    def perimeter(self):
        """Calculate and return the perimeter of the square"""
        return self.side * 4
    
    def diagonal(self):
        """Calculate and return the diagonal of the square"""
        return math.sqrt(2 * self.side ** 2)
    
    
    