# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:02:56 2021.

Keeping student exam records in a csv file

@author: Tindi.Sommers
"""
import csv

print('Enter ~ at the end of your records.')
while True:
    record = []
    first_name = input('Enter Student first name: ')
    if first_name == '~':
        break
    else:
        record.append(first_name)
    surname = input('Enter student surname: ')
    record.append(surname)
    grade1 = int(input('Enter first grade. Must be an integer: '))
    record.append(grade1)
    grade2 = int(input('Enter 2nd grade. Must be an integer: '))
    record.append(grade2)
    grade3 = int(input('Enter 3rd grade. Must be an integer: '))
    record.append(grade3)

    # record the student record in the csv file
    with open('grades.csv', 'a', newline='') as grades:
        writer = csv.writer(grades)
        writer.writerow(record)

