# -*- coding: utf-8 -*-
"""
Created on Mon May  3 16:07:14 2021.

A bar chart of trending topics on Twitter

@author: Tindi.Sommers
"""
import tweepy
import keys
import pandas as pd

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

trends = api.trends_place(id=23424908)

trends_list = trends[0]['trends']

trends_list = [t for t in trends_list if t['tweet_volume']]

df = pd.DataFrame(trends_list)
print(df.head())

axes = df.plot.bar(x='name', y='tweet_volume', legend=False)
