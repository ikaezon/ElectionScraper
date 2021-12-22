import tweepy
import pandas as pd
import time

consumer_key = "41LOHNflVvMgGXhX3sUYijYOF"
consumer_secret = "Lf84X0ITngmRHIITd898ohtXGmmF1wRub0xeDbznBHQK8CxVls"
access_token = "4922479265-g08Zrl2wys5sFgCbikk2RPjRT9fNO2VL9VssA5x"
access_token_secret = "aJWjrMvulCZjQNLCL0tVRBo1Tcq7WPi0uTWD6aKTGxvng"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []
username = input("Enter username: ")
tweets_num = int(input("How many tweets: "))

def tweets_to_csv(username, tweets_num):
    for tweet in api.user_timeline(id=username, count=tweets_num):
        tweets.append((tweet.created_at, tweet.id, tweet.text))
        data_frame = pd.DataFrame(tweets, columns=['Date', 'Tweet_ID', 'Message'])
        data_frame.to_csv('kaevon_scraped.csv')


tweets_to_csv(username, tweets_num)