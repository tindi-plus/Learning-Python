# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 15:07:02 2021.

Using the NaiveBayesAnalyzer

@author: Tindi.Sommers
"""
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
from textblob.sentiments import NaiveBayesAnalyzer

response = requests.get("https://edition.cnn.com/2021/04/12/china/china-maritime-militia-explainer-intl-hnk-ml-dst/index.html")

soup = BeautifulSoup(response.content, 'html.parser')
text = soup.get_text(strip=True) # extract the text from the html tags


blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

# get the sentiment of the news article
sentiment = blob.sentiment 

print(sentiment)
print()

print('Sentiment for each of the Sentences')
print()

for sentence in blob.sentences:
    print(f'The sentiment of the sentence \'{sentence}\' is: {sentence.sentiment}')
    print()
