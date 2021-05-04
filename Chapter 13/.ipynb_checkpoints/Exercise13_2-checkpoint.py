# -*- coding: utf-8 -*-
"""
Created on Mon May  3 10:58:31 2021.

Percentage of retweets

@author: Tindi.Sommers
"""

import tweepy
import keys

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#search and grab tweets about liverpool
cursor = tweepy.Cursor(api.search, q='liverpool', count=100)

retweets = 0

for tweet in cursor.items(1000):
    if tweet.text.startswith('RT'):
        retweets += 1

print(f'Percentage of retweets are: {retweets / 1000:.2%}')