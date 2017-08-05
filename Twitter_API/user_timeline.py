import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = '1234xyz'
CONSUMER_SECRET = '1234xyz'
OAUTH_TOKEN = '1234xyz'
OAUTH_TOKEN_SECRET = '1234xyz'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print status.text