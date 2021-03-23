# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:34:01 2021.

Reading a csv file online.

@author: Tindi.Sommers
"""
import csv

# get the csv file
with open('TitanicSurvival.csv', 'r') as titanic:
    reader = csv.DictReader(titanic, fieldnames=['Names', 'Survived', 'Sex', 'Age', 'Class'])
    age_count = 0
    age_sum = 0
    for row in reader:
        if row['Age'].isnumeric():
            age_sum += float(row['Age'])
            age_count += 1

avg_age = age_sum / age_count
print(f'The average age is {avg_age:,.2f}')