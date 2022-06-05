# coding: UTF-8
from evernote_bot import evernote_api, twitter_api, tag_control

#ノートブックを指定
selected_notebook_name='test'

#ランダムにノートを取得する
selected_note=evernote_api.getNoteContents(selected_notebook_name)

print(selected_note['title'])
print('--------------------')

#textを抽出
print( tag_control.getText(selected_note['text']) )
print('--------------------')

#commentを抽出
print( tag_control.getComment(selected_note['text']) )
print('--------------------')

#タグをハッシュタグのテキストに変更する
print(tag_control.getHashTag( selected_note['tags'] ))
print('--------------------')

#タイトル ハッシュタグを含めた140文字を最初に選び、140文字ごとのテキストのリストを作成する