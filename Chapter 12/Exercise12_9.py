# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:00:14 2021.

Similarity detection with spaCy

@author: Tindi.Sommers
"""

import spacy
import requests
from bs4 import BeautifulSoup

raw_news = requests.get("https://www.africanews.com/2021/04/17/cape-verde-final-colourful-campaigns-before-parliamentary-election/")
raw_news2 = requests.get('https://www.aljazeera.com/news/2020/8/4/dozens-killed-as-huge-explosion-rips-through-lebanons-beirut')

soup = BeautifulSoup(raw_news.content, 'html.parser')
soup2 = BeautifulSoup(raw_news2.content, 'html.parser')
news = soup.get_text(separator=' ', strip=True)
news2 = soup2.get_text(separator=' ', strip=True)

print(news)
print()
print(news2)

nlp = spacy.load('en_core_web_sm')
nlp2 = spacy.load('en_core_web_sm')

article = nlp(news)
article2 = nlp2(news2)

# compare for similarity between article and article2
similarity = article.similarity(article2)
print(similarity)