# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 13:08:57 2021.

Named entity recognition with spaCy

@author: Tindi.Sommers
"""
import spacy
import requests
from bs4 import BeautifulSoup

raw_news = requests.get("https://www.africanews.com/2021/04/17/cape-verde-final-colourful-campaigns-before-parliamentary-election/")

soup = BeautifulSoup(raw_news.content, 'html.parser')
news = soup.get_text(separator=' ', strip=True)

nlp = spacy.load('en_core_web_sm')
article = nlp(news)

# get all the named entities and print them
for entity in article.ents:
    print(f'{entity.text}: {entity.label_}')
