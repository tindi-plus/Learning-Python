# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:06:31 2021.

Word Frequency Bar chart

@author: Tindi.Sommers
"""
import pandas as pd
from pathlib import Path
from textblob import TextBlob
import imageio
from nltk.corpus import stopwords
from operator import itemgetter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# use path to read the text from the file
text = Path('The Hamlet_The Prince of Denmark.txt').read_text()

# create a textblob object with the text
blob = TextBlob(text)

# create a stopwords object in english
stops = stopwords.words('english')

# obtain the dictionary of the word counts
items = blob.word_counts.items()

# use list generator to select the words that do not appear in the stopwords list
words = [item for item in items if item[0] not in stops]

# sort the words based on their frequency
sorted_words = sorted(words, key=itemgetter(1), reverse=True)

# pick the top 20 words
top20 = sorted_words[0:20]

# create a dataframe of the words
df = pd.DataFrame(top20, columns=['Words', 'Counts'])

# create a bar plot using dataframe's bar plot
axes = df.plot.bar(x='Words', y='Counts', legend=False)

# ensure that the layout is tight, showing all words fully
plt.gcf().tight_layout()

# get the image to be used for the wordcloud
image_mask = imageio.imread('mask_oval.png')

# create the word cloud object
wordcloud = WordCloud(colormap='prism', mask=image_mask)

# generate the wordcloud
word_image = wordcloud.generate(text)

# save the image to a file
word_image.to_file('Hamlet_oval_image.png')


