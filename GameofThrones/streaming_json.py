# Prepare Environment

## Import JSON library
try:
    import json
except ImportError:
    import simplejson as json

## Import "twitter" library
from twitter import *

## Set up credentials to access Twitter API
ACCESS_TOKEN = '85621908-Mi8AHFgdxfgz6crNIpHvomR9qYzIG8u696EQY73Tv'
ACCESS_SECRET = 'YQ5dR4P2UChL8n7PLbyT2maVUTmZgcrhEi5yJo4xE1JAb'
CONSUMER_KEY = 'W26R2xhOik4m3tpqqcB1krwjZ'
CONSUMER_SECRET = 'yaJhOEmVR3VDRwDBVaAaCKgnHDLu6RpxfyM2I5qaj1bZu1Q6ah'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

## Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth = oauth)

# Start to streaming

## Set filtering key words
## Limit tweets language equals to English
search = "#GameofThrones"
iterator = twitter_stream.statuses.filter(track = search, language = "en")

## Set the number of tweets
tweet_count = 1000

# Streaming tweets
for tweet in iterator:
    tweet_count -= 1

    ## Python Twitter Tools will wrap-up 1000 tweets with #GameofThrones
	## to the JSON format and show them on the screen
    print json.dumps(tweet)  

    if tweet_count <= 0:
        break
