# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:26:09 2021
Telephone number word generator
@author: Tindi.Sommers
"""

# Request for the phone number the user wants to generate words for
phone_num = input('Enter the phone number you want to generate words for: ')

num_all = '23456789'
num_list = []
num_list += phone_num  # convert the string input into a list

check = True
# verify that the input is a seven digit string
while (check):
    for i in num_list:
        if i not in num_all:
            phone_num = input('''The phone number you entered is not correct.
                  Enter a 7 digit phone number: ''')
            num_list = []
            num_list += phone_num
            check = True
            break
        else:
            check = False

# find the corresponding alphabets for each number
all_letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs', 'tuv', 'wxy']

# get a list of group of letters that phone number represent
letters = []
for index, value in enumerate(phone_num):
    x = num_all.index(value)  # obtain the index of value in num_all
    letters.append(all_letters[x])

# now iterate through all the corresponding letters and find possible words
for a in letters[0]:
    for b in letters[1]:
        for c in letters[2]:
            for d in letters[3]:
                for e in letters[4]:
                    for f in letters[5]:
                        for g in letters[6]:
                            print(a + b + c + d + e + f + g)
