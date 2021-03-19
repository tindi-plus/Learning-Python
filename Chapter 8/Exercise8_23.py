# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 19:59:33 2021.

Spam email detection

@author: Tindi.Sommers
"""
# list of spam words and phrases

spam_words = ['Act now', 'casino', 'apply now', 'cash', 'buy', 'bonus', 'boss',
              'cancel', 'additional income', 'friend', 'great', 'income',
              'earn', 'lose', 'junk', 'luxury', 'open', 'purchase', 'refund',
              'free', 'extra', 'limited', 'hello', 'instant', 'urgent',
              'save', 'take action', 'winner', 'terms', 'trial', 'score',
              'obligation', 'only', 'please', 'money', 'unlimited', 'deal',
              'supplies', 'request', 'promise', 'no credit', 'refund']
# get email from user
email = input('Please input your email to check for spam: ')
# check the number of spam words that are in the email
count = 0
for word in spam_words:
    if word in email:
        count += 1

print()
print(count)
if count > 5 and count < 10:
    print('The email is very likely to be spam.')
elif count > 10:
    print('The email is definately spam!')
else:
    print('The email is not spam.')


