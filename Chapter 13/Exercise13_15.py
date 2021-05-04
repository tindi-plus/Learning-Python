# -*- coding: utf-8 -*-
"""
Created on Tue May  4 11:04:19 2021.

Creating a heat map with folium

@author: Tindi.Sommers
"""

from tweetutilities import get_API
from locationlistener import LocationListener
import tweepy
from tweetutilities import get_geocodes
import pandas as pd
import folium
from folium import plugins

api = get_API()

tweets = []
counts = {'total_tweets': 0, 'locations': 0}

location_listener = LocationListener(api, counts_dict=counts,
                                     tweets_list=tweets, topic='football', limit=100)

stream = tweepy.Stream(auth=api.auth, listener=location_listener)
stream.filter(track=['football'], languages=['en'], is_async=False)

counts['total_tweets']
counts['locations']

bad_locations = get_geocodes(tweets)

df = pd.DataFrame(tweets)
df = df.dropna()

heat_map = folium.Map(location=[9.0845755, 8.674252],
                   tiles='Stamen Terrain', zoom_start=5, detect_retina=True)

coordinates = []

for t in df.itertuples():
    
    coordinates.append([t.latitude, t.longitude])

hm = plugins.HeatMap(coordinates)
heat_map.add_child(hm)

heat_map.save('tweets_heatmap.html')

