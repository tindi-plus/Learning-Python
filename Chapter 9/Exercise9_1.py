# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 23:18:51 2021.

Writing grades to a text file

@author: Tindi.Sommers
"""
# create the grades_avg file for storing the grades
with open('grades_avg.txt', 'a') as grades:
    while True:  # get the grades from user untill they input ~
        grade = input('Enter the grade. Enter ~ if you there are no more grades to enter: ')
        if grade == '~':
            break  # exit the while loop
        else:
            grades.write(grade + '\n')  # add the grade to file
