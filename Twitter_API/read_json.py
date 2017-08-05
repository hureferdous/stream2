import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'


def read_json(file_path):
    results = []
    tweets_file = open(file_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False