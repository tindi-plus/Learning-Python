# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:02:56 2021.

Keeping student exam records in a csv file

@author: Tindi.Sommers
"""
import csv
import json

print('Enter ~ at the end of your records.')
# list of student dictionaries
record = []
while True:
    student_dict = {}
    first_name = input('Enter Student first name: ')
    if first_name == '~':  # check if input is end of records, exit while loop
        break
    else:
        student_dict['First Name'] = first_name
    surname = input('Enter student surname: ')
    student_dict['surname'] = surname
    grade1 = int(input('Enter first grade. Must be an integer: '))
    student_dict['exam1'] = grade1
    grade2 = int(input('Enter 2nd grade. Must be an integer: '))
    student_dict['exam2'] = grade2
    grade3 = int(input('Enter 3rd grade. Must be an integer: '))
    student_dict['exam3'] = grade3
    # add the dictionary to the record of students
    record.append(student_dict)


# record the student records in the json file
with open('grades2.json', 'a') as grades:
    # create a dictionary of the student records and write it to a json file
    json.dump({'students': record}, grades)
