# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:35:57 2021
Writing the word equivalent of a check amount
@author: Tindi.Sommers
"""

digits = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR', 5: 'FIVE', 6: 'SIX',
          7: 'SEVEN', 8: 'EIGHT', 9: 'NINE', 0: 'ZERO'}

place_value = {0: '', 1: 'TEN', 2: 'HUNDRED', 3: 'THOUSAND'}

stage2 = {10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN',
          14: 'FOURTEEN', 15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN',
          18: 'EIGHTEEN', 19: 'NINETEEN'
          }
stage3 = {2: 'TWENTY', 3: 'THIRTY', 4: 'FOURTY', 5: 'FIFTY', 6: 'SIXTY',
          7: 'SEVENTY', 8: 'EIGHTY', 9: 'NINETY', 0: ''}

check = input('Input the check amount in numbers: ')
check_split = check.split('.')
whole_number = check_split[0]
float_number = check_split[1]

num_list = []
num_list += whole_number

check_num = [int(i) for i in num_list]  # create a list of integers from num_list

check_in_words = ''  # placeholder for the check amount in words

# the for statement matches each number with the dictionaries above to pick the
# corresponding word for each number
for index, value in enumerate(check_num):
    if len(check_num) - 1 - index >= 2:
        check_in_words += digits[value] + ' ' + place_value[len(check_num) - index - 1] + ' '
    elif index == len(check_num) - 1:
        continue
    else:
        check_in_words += 'AND '
        if value == 1:
            check_in_words += stage2[value * 10 + check_num[len(check_num) - 1]] + ' '
        else:
            check_in_words += stage3[value] + ' ' + digits[check_num[len(check_num) - 1]] + ' '

check_in_words += f'{float_number}/100'
print(check_in_words)
