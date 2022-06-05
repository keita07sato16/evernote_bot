# coding: UTF-8
from evernote_bot import evernote_api, twitter_api, tag_control

def main():
    #ノートブックを指定
    selected_notebook_name="最初のノートブック"
 
    #ランダムにノートを取得する
    selected_note=evernote_api.getNoteContents(selected_notebook_name)
    
    #tweetする function tweet(title, text, comment, tag)
    tweet_title=selected_note["title"] 
    
    print(selected_note["text"])
    print("-------------------")
    print(tweet_title)
                         
    tweet_texts_commnets=tag_control.getTextsComments(selected_note["text"])
    tweet_text=tag_control.appnedTextTag(tweet_texts_commnets["tweet_text"], selected_note["tags"])
    print(tweet_text)

    for comment in tweet_texts_commnets["tweet_comments"]:
        print(comment)