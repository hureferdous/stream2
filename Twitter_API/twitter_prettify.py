from prettytable import PrettyTable

import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter

# Replace these values with our own twitter app settings
CONSUMER_KEY = '1234xyz'
CONSUMER_SECRET = '1234xyz'
OAUTH_TOKEN = '2535164173-1234xyz'
OAUTH_TOKEN_SECRET = '1234xyz'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags'] ]

words = [ w for t in status_texts
         for w in t.split() ]


for label, data in (('Text', status_texts),
                    ('Screen Name', screen_names),
                    ('Word', words)):
    table = PrettyTable(field_names=[label, 'Count'])
    counter = Counter(data)
    [ table.add_row(entry) for entry in counter.most_common()[:10] ]
    table.align[label], table.align['Count'] = 'l', 'r' # align the columns
    print table