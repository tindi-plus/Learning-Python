# -*- coding: utf-8 -*-
"""
Created on Mon May  3 14:18:32 2021.

Condensing tweets and writing them to a csv file

@author: Tindi.Sommers
"""
import tweepy
import keys
import pandas as pd

#authenticate with Twitter and create an api
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

cursor = tweepy.Cursor(api.search, q='chelsea', count=50)

condensed = {'ID':[], 'Name': [], 'Created_at': [], 'Text': []}

for t in cursor.items(limit=50):
    condensed['ID'].append(t.id_str)
    condensed['Name'].append(t.user.name)
    condensed['Created_at'].append(t.created_at)
    condensed['Text'].append(t.text)

# write the dataframe to a csv file
df = pd.DataFrame(condensed)
df.to_csv('condensed_tweets.csv')