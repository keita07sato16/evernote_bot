# coding: UTF-8

import tweepy
import random

CONSUMER_KEY = "BhkGKCWAUUa6lYyaR1pFWPCj2"
CONSUMER_SECRET = "UCSv5Hny6Q0q5kRgqSy93x1SoFqwy4QiFnMxHoQGqumkIZsht4"
ACCESS_TOKEN = "1517019252284600321-qd4OB3WIFMcSCbvSb3QGGngXIuKjeb"
ACCESS_TOKEN_SECRET = "hLv9DZBWYa8udk4mmtUlHqXc2ShCowvSZ0nRVRiSwkh78"


#ツイートする文字列

STATUS_DATA = [
    "1つ目のメッセージ",
    "2つ目のメッセージ",
    "3つ目のメッセージ"
]


def tweet(text):
    makeApi().update_status(text)

def getLatestTweet():
    return makeApi().home_timeline()

def makeApi():
    #Return tweepy.API object

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

if __name__ == "__main__":
   print ( getLatestTweet()[0].text )