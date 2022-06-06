# coding: UTF-8
import tweepy
import datetime
import random
import unicodedata as uni
import re

CONSUMER_KEY = "BhkGKCWAUUa6lYyaR1pFWPCj2"
CONSUMER_SECRET = "UCSv5Hny6Q0q5kRgqSy93x1SoFqwy4QiFnMxHoQGqumkIZsht4"
ACCESS_TOKEN = "1517019252284600321-qd4OB3WIFMcSCbvSb3QGGngXIuKjeb"
ACCESS_TOKEN_SECRET = "hLv9DZBWYa8udk4mmtUlHqXc2ShCowvSZ0nRVRiSwkh78"

def tweet(text):
    makeApi().update_status(text)

def getLatestTweet():
    return makeApi().home_timeline()

def makeApi():
    #Return tweepy.API object
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def len_fullwidth(text):
    return -(-sum([(1, 2)[uni.east_asian_width(t) in 'FWA'] for t in text])//2)

def makeInitTweet(title, text, tag):
  _init_tweet = title + tag
  init_tweet = ''

  if len_fullwidth(_init_tweet + text)<=140:
    print('OK, Tweet!')
    print(title + text + tag)

  else:
    _text_list = []
    _text_list = text.split('。')

    for idx in range(len(_text_list)):
      if re.match(r'^[\n]+$', _text_list[idx]) == None:
        _text_list[idx] += '。'

    if len_fullwidth(_init_tweet + _text_list[0]) > 140:
      print('Only, Title')
      print(title)
    
    else:
      init_tweet = title + _text_list[0]
      for idx in range(1, len(_text_list)):
        if len_fullwidth( init_tweet + _text_list[idx] + tag) > 140:
            init_tweet += tag
            print(len(init_tweet))
            print(init_tweet)

            return _text_list[idx: len(_text_list)]
        
        else:
          init_tweet += _text_list[idx]

def testTweet():
  i=1

  today = datetime.date.today() #.strftime('%Y/%m/%d')
  just_now = datetime.datetime.now()

  while i<20:
    api.update_status("test" +str(i) + "\n\n" + just_now.strftime("%Y/%m/%d %H:%M:%S"))
    
    #最新のツイートへリプライを行う
    latest_tweet_id=api.user_timeline(id="yEHqc2h6R5sJEbf")[0].id
    api.update_status("replay", latest_tweet_id)

    i+=1

def MultiTweet(tweet_text):
  if len(tweet_text) <=140:
    print('OK, Tweet')
  else:
    _tweet_list=tweet_text.split('。')

    safe_tweet=_tweet_list[0] + '。'
    tweet_list=[]

    if len(safe_tweet) > 140 :
      print('Too Long')
      
    else:
      for idx in range(len(_tweet_list)):
        if idx == len(_tweet_list)-1:
          safe_tweet=safe_tweet[::-1]
          safe_tweet=safe_tweet.replace('。', '', 1)
          safe_tweet=safe_tweet[::-1]

          tweet_list.append(safe_tweet)
        else:
          if len( safe_tweet + _tweet_list[idx+1] + '。') > 140:
            tweet_list.append(safe_tweet)
            safe_tweet=_tweet_list[idx+1] + '。'
          else:
            safe_tweet += _tweet_list[idx+1] + '。'

  return tweet_list

