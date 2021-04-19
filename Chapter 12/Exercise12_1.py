# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 20:37:49 2021

web scrapping using Beautiful Soup and requests module

@author: Tindi.Sommers
"""
from bs4 import BeautifulSoup
import requests
from wordcloud import WordCloud
import imageio

# scrape data from https://www.python.org

response = requests.get('https://www.python.org')

# extract the text from the html tags using Beautiful Soup
soup = BeautifulSoup(response.content, 'html5lib')
text = soup.get_text(strip=True)

# get the image to be used for a word cloud 
mask_image = imageio.imread('mask_circle.png')

# create the wordcloud object with the desired attributes
wordcloud = WordCloud(colormap='prism', mask=mask_image)

# generate the word cloud using the wordcloud object
word_cloud = wordcloud.generate(text) 

# save the generated word cloud to a file named python.png
word_cloud.to_file('python.png')

# WordCloud usually removes all stop words before drawing the word cloud.

