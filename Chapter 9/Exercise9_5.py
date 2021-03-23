# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:42:45 2021.

Creating a report from grades.csv.

@author: Tindi.Sommers
"""
import csv
import pandas as pd

# read the csv data and load it into a dataframe
grades = pd.read_csv('grades.csv', names=['First Name', 'Surname', 'Grade1',
                                          'Grade2', 'Grade3'])
pd.set_option('precision', 2)

student_avg = grades.mean(axis=1)  # get the average of each student
# add a new column called average at location 5 of the dataframe
grades.insert(5, 'Average', student_avg)
# get the average of each course or grade
grade_avg = grades.mean(axis=0)
# append the grades average at the bottom of the dataframe
grades = grades.append(grade_avg, ignore_index=True)
print(grades)