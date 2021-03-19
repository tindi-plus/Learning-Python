# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:35:34 2021.

Verify the strenght of a password

@author: Tindi.Sommers
"""
import re
# define the various parameters the password must meet
lenghtRegex = re.compile(r'\w{8,}')
lowerRegex = re.compile(r'[a-z]+')
upperRegex = re.compile(r'[A-Z]+')
digitRegex = re.compile(r'[0-9]+')
specialRegex = re.compile(r"[@#%&*$!<>?+_*=']+")

passLow = True  # current password strength is low


def pass_strength():
    """Verify that the password meets all the defined rules."""
    password = input("""Input your password. Password must be at least 8
                     characters long and must contain 1 upper case,
                     1 lower case, 1 digit and 1 special character
                     such as !@#$%&*+=_<>?:' """)
    # if password does not have 8 characters
    if lenghtRegex.findall(password) == []:
        print('Password must have at least 8 characters')
    elif lowerRegex.findall(password) == []:
        print('Password must contain at least one lower case')
    elif upperRegex.findall(password) == []:
        print('Password must contain at least one upper case')
    elif digitRegex.findall(password) == []:
        print('Password must contain at least one digit')
    elif specialRegex.findall(password) == []:
        print('Password must contain at least one special character')
    else:
        print('You have a strong password!')
        global passLow
        passLow = False

    while passLow:
        pass_strength()

pass_strength()




