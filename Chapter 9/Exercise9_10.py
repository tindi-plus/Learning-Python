# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:03:03 2021.

Reading text from a text file (Pride Prejudice)

@author: Tindi.Sommers
"""

import re
from collections import Counter

# read the text from Pride Prejudice.txt
with open('Pride and Prejudice.txt', 'r', encoding='utf8') as pride:
    pride_prejudice = ''
    for line in pride:
        pride_prejudice += line

# split the pride_prejudice into words using any white space character
words = re.findall(r'[A-Za-z]+', pride_prejudice)
word_count = len(words)
print(f'Total word count is: {word_count:,}')

# get the total number of characters in the pride_prejudice including white spaces
char_count = 0
for char in pride_prejudice:
    char_count += 1
print(f'Total characters: {char_count:,}')
print()

# average word length will be given by total number of characters without
# white spaces divide by the total number of words
char_count_no_space = len(re.findall(r'\w', pride_prejudice))
avg_word_len = char_count_no_space / word_count
print(f'Average word length: {avg_word_len:,.1f}')
print()

# get the average sentence length
sentences = re.split(r'\.\s', pride_prejudice)
words_in_sentence = 0
for sentence in sentences:
    words_in_sentence += len(re.split(r' ', sentence))

avg_sen_len = words_in_sentence / len(sentences)
print(f'Average sentence length is {avg_sen_len:,.2f} words.')
print()

# get the word distribution of all the words
print(Counter(words))
print()

# get the 10 longest words
word_lengths = {}
for word in words:
    word_lengths[word] = len(word)
# sort the dictionary based on the values in a descending order
words_sorted = sorted(word_lengths.items(), key=lambda x: x[1], reverse=True)
print('The 10 longest words are: ', end=' ')
for i in range(10):
    print(words_sorted[i], end=' ')
