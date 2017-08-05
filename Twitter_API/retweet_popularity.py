import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable
from operator import itemgetter

CONSUMER_KEY = 'abc123'
CONSUMER_SECRET = 'abc123'
OAUTH_TOKEN = 'abc123'
OAUTH_TOKEN_SECRET = 'abc123'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 150
query = 'Ireland'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]