# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:19:10 2021.

Readability assessment with Textatistic

@author: Tindi.Sommers
"""
import requests
from textatistic import Textatistic
from bs4 import BeautifulSoup

# scrape the Internet for news articles
news_fox = requests.get('https://www.foxnews.com/world/explosion-lebanon-capital-beirut')
news_thesun = requests.get('https://timesofindia.indiatimes.com/world/middle-east/massive-beirut-blast-kills-more-than-70-injures-thousands/articleshow/77360097.cms')
news_aljazeera = requests.get('https://www.aljazeera.com/news/2020/8/4/dozens-killed-as-huge-explosion-rips-through-lebanons-beirut')

# create BeautifulSoup objects for the news articles
soup_fox = BeautifulSoup(news_fox.content, 'html.parser')
soup_thesun = BeautifulSoup(news_thesun.content, 'html.parser')
soup_aljazeera = BeautifulSoup(news_aljazeera.content, 'html.parser')

# get the text from the html pages in Beautiful Soup
text_fox = soup_fox.get_text(separator=' ', strip=True)
text_thesun = soup_thesun.get_text(separator=' ', strip=True)
text_aljazeera = soup_aljazeera.get_text(separator=' ', strip=True)

print(text_thesun)

# Check the readability using Textatistics
readability_fox = Textatistic(text_fox)
readability_thesun = Textatistic(text_thesun)
readability_aljazeera = Textatistic(text_aljazeera)

print(f'The readability for Fox News is: {readability_fox.notdalechall_count}')
print(f'The readability for The Sun News is: {readability_thesun.notdalechall_count}')
print(f'The readability for Aljazeera News is: {readability_aljazeera.notdalechall_count}')
