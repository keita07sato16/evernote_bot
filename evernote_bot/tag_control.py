# coding: UTF-8
def getContents(_note_text):
  _text_list = []

  start_target = '<div>'
  end_target = '</div>'
  
  start_index = _note_text.find(start_target)+len(start_target)
  end_index = _note_text.find(end_target)
  
  while start_index-len(start_target)>=0 and end_index>=0 :
    _text_list.append(_note_text[start_index: end_index])
    _note_text = _note_text[end_index+len(end_target) :]
    start_index = _note_text.find(start_target)+len(start_target)
    end_index = _note_text.find(end_target)

  contents_text=''

  for _text in _text_list:
    #ここに改行を入れる処理を加えるかも
    contents_text += _text

  return contents_text

def getText(_note_text):
  note_text = getContents(_note_text)

  if note_text.find('<comment>') != -1:
    note_text=note_text[:note_text.find('<comment>')]

  return note_text

def getComment(_note_text):
  comment_text_list=[]

  start_target = '<comment>'
  end_target = '</comment>'
  
  start_index = _note_text.find(start_target)+len(start_target)
  end_index = _note_text.find(end_target)
  
  while start_index-len(start_target)>=0 and end_index>=0 :
    comment_text_list.append(_note_text[start_index: end_index])
    _note_text = _note_text[end_index+len(end_target) :]
    start_index = _note_text.find(start_target)+len(start_target)
    end_index = _note_text.find(end_target)

  return comment_text_list

def getHashTag(note_tag_list):
  hash_tag_text = ''

  if note_tag_list != None:
    for note_tag in note_tag_list:
      hash_tag_text += '#' + note_tag + ' '
  
  return hash_tag_text