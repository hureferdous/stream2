import json
import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = '1234xyz'
CONSUMER_SECRET = '1234xyz'
OAUTH_TOKEN = '2535164173-1234xyz'
OAUTH_TOKEN_SECRET = '1234xyz'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 10
query = 'Dublin'

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

for result in results:
    print result


def get_lexical_diversity(items):
   return 1.0 * len(set(items)) / len(items)


def get_average_words(tweets):
    total_words = sum([len(tweet.split()) for tweet in tweets])
    return 1.0 * total_words / len(tweets)


    print "Average words: %s" % get_average_words(status_texts)
    print "Word Diversity: %s" % get_lexical_diversity(words)
    print "Screen Name Diversity: %s" % get_lexical_diversity(screen_names)
    print "HashTag Diversity: %s" % get_lexical_diversity(hashtags)