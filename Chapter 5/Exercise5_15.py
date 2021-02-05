# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:00:10 2021
Code for sorting invoices
@author: Tindi.Sommers
"""
from operator import itemgetter

invoice_list = [(83, 'Electric Sander', 7, 57.98),
                (24, 'Power Saw', 18, 19.99),
                (7, 'Sledge Hammer', 11, 21.50),
                (77, 'Hammer', 76, 11.99),
                (39, 'Jig Saw', 3, 79.50)]
a = sorted(invoice_list, key=itemgetter(0))
print(a)
print()

b = sorted(invoice_list, key=itemgetter(3))
print(b)
print()

mapped = list(map(lambda x: (x[0], x[2]), invoice_list))
print(mapped)
c = sorted(mapped, key=itemgetter(1))
print(c)
print()

mapped_d = list(map(lambda x: (x[0], x[2]*x[0]), invoice_list))
d = sorted(mapped_d, key=itemgetter(1))
print(d)
print()

mapped_e = list(filter(lambda x: x[1] > 200 and x[1] < 500, mapped_d))
e = sorted(mapped_e)
print(e)
