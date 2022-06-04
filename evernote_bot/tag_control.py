# coding: UTF-8
def getTextsComments(_text) :
  _text_list = []

  start_target = "<div>"
  end_target = "</div>"
  
  start_index = _text.find(start_target)+len(start_target)
  end_index = _text.find(end_target)
  
  while start_index-len(start_target)>=0 and end_index>=0 :
    _text_list.append(_text[start_index: end_index])
    _text = _text[end_index+len(end_target) :]
    start_index = _text.find(start_target)+len(start_target)
    end_index = _text.find(end_target)

  comment_list=[]
  text_list=[]

  for text in _text_list:
    if text.startswith("comment"):
      comment_list.append(text[8:].replace('<br clear="none"/>', ''))
      _text_list.remove(text)
    else:
      text_list.append(text.replace('<br clear="none"/>', ''))
  
  tweet_text="\n".join(text_list)

  tweet_contents=dict()
  tweet_contents["tweet_text"]=tweet_text
  tweet_contents["tweet_comments"]=comment_list

  return tweet_contents

def appnedTextTag(text, tag_list):
  text+="\n\n"

  if tag_list != None:
    for tag in tag_list:
      text+="#"+tag+" "
  
  return text

""""
def getComments(_comment_text) :
  comment_list = []

  start_target = "<comment>"
  end_target = "</comment>"
  
  start_index = _comment_text.find(start_target)+len(start_target)
  end_index = _comment_text.find(end_target)
  
  while start_index-len(start_target)>=0 and end_index>=0 :
    comment_list.append(_comment_text[start_index: end_index])
    _comment_text = _comment_text[end_index+len(end_target) :]
    start_index = _comment_text.find(start_target)+len(start_target)
    end_index = _comment_text.find(end_target)

  return comment_list
"""
"""
def getText(_note_text):
  start_target = "<div>"
  end_target = "</div>"
  
  start_index = _note_text.find(start_target)+len(start_target)
  end_index = _note_text.find(end_target)
  
  note_text=_note_text[start_index: end_index]

  return note_text
"""