# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:25:26 2021.

Munging date formats. The user sends in text with date different date formats and
the scripts picks the dates and changes them from one format into the other.
The formats are:
042592
04/25/1992
April 25, 1992.
Example: You can call me on 031599 or 09/22/1999 or December 10, 1999

@author: Tindi.Sommers
"""
import re
# create patterns for the different date formats
first_date = re.compile(r'[0-9]{6}')
second_date = re.compile(r'\d\d/\d\d/\d{4}')
third_date = re.compile(r'[A-Z][a-z]+ \d\d, \d{4}')

months = 'January01, February02, March03, April04, May05, June06, July07, August08, September09, October10,November11, December12'


text = input('Input your text with dates: ')
# find the first dates and convert them to the other dates
if first_date.findall(text):
    for i in first_date.findall(text):
        print(i)
        # capture parts of the date
        result = re.fullmatch(r'(\d\d)(\d\d)(\d\d)', i)
        # combine the parts to form date of the format 04/25/1955
        new_date1 = result.group(1) + '/' + result.group(2) + '/19' + result.group(3)
        print(new_date1)
        # pick the month in words
        result2 = re.search(r'(\w+)' + result.group(1), months)
        print(result2.group(1) + ' ' + result.group(2) + ', 19' + result.group(3))
        print()

# find the second date and change it into the first and third date formats
if second_date.findall(text):
    for i in second_date.findall(text):
        # remove the slashes and the 19
        print(re.sub(r'/19|/', '', i))
        # get the parts of the dates
        date_parts = re.split(r'/', i)
        # get the month in words
        result = re.search(r'(\w+)' + date_parts[0], months)
        print(result.group(1) + ' ' + date_parts[1] + ', ' + date_parts[2])
        print()

# find the third date and change it into the first and second date formats
if third_date.findall(text):
    for i in third_date.findall(text):
        # get the different parts of the date
        result = re.search(r'(\w+) (\d\d), \d\d(\d\d)', i)
        print(result.group())
        # get the month in figures
        month_figure = re.search(result.group(1) + r'(\d\d)', months)
        # print date in first date format
        print(month_figure.group(1) + result.group(2) + result.group(3))
        # print the date in the second date format
        print(month_figure.group(1) + '/' + result.group(2) + '/19' + result.group(3))
        print()







