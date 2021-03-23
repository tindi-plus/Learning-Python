# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:42:27 2021.

Visualising word frequencies with word clouds.

@author: Tindi.Sommers
"""
from wordcloud import WordCloud
import re
from collections import Counter

# read the text from Pride Prejudice.txt
with open('Pride and Prejudice.txt', 'r', encoding='utf8') as pride:
    pride_prejudice = ''
    for line in pride:
        pride_prejudice += line

# split the pride_prejudice into words using any white space character
words = re.findall(r'[A-Za-z]+', pride_prejudice)

# get the word distribution of all the words
# print(Counter(words))
# print()
word_freq = {}
for i in Counter(words).most_common(200):
    x, y = i
    word_freq[x] = y

wordcloud = WordCloud(colormap='prism', background_color='white')
wordcloud = wordcloud.fit_words(word_freq)
wordcloud = wordcloud.to_file('PrideandPrejudice.png')

