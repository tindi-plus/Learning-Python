# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:59:30 2021.

Analyzing tweets to form opinions about the stock market

@author: Tindi.Sommers
"""
from textblob import TextBlob
import tweepy
import keys
import preprocessor as p
from textblob.utils import lowerstrip

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# the search api can return a maximum of 100 results at a time
cursor = tweepy.Cursor(api.search, q='to:apple', count=100)

# a dict for storing the positive and negative sentiments
sentiment = {'positive':0, 'negative':0}

# get a total of 1000 tweets from the cursor object
for tweet in cursor.items(1000):
    # try to get the extended tweet if the tweet is above 140 characters
    try:
        tweet_text = tweet.extended_tweet.text
    except:
        tweet_text = tweet.text
    
    # clean the text and pass it on to TextBlob
    blob = TextBlob(p.clean(tweet_text))
    
    # check the sentiment of the tweet and increment the value appropriately
    # in the sentiment dict
    if blob.sentiment.polarity >= 0:
        sentiment['positive'] += 1
    else:
        sentiment['negative'] += 1

# make a decision based on the result of the sentiment analyses
if sentiment['positive'] > sentiment['negative']:
    print('The market sentiment for apple is positive. It is a good time to buy.')
else:
    print('The market sentiment for apple is negative. It is not a good time to buy.')

print(sentiment)