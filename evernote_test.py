# coding: UTF-8
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.UserStore
import evernote.edam.notestore.NoteStore
import evernote.edam.userstore.constants
import evernote.edam.notestore.ttypes as NSTypes
import evernote.edam.type.ttypes as Types
import random

sandboxToken='S=s1:U=96a6d:E=1877ab73600:C=18023060a00:P=1cd:A=en-devtoken:V=2:H=3491c0b98b41a4ded1ceb841e7844d5f'
client=EvernoteClient(token=sandboxToken)
noteStore=client.get_note_store()
choiceNotebookName="最初のノートブック"

def getNotebookGuidByName(notebookName):
    notebooks=noteStore.listNotebooks()

    for notebook in notebooks:
        if notebook.name == notebookName :
            notebookGuid=notebook.guid

    return notebookGuid

def randomSelectNote(notebookGuid):
     # 検索条件設定：指定ノートブックにひも付くノート
    filter = NSTypes.NoteFilter()
    filter.notebookGuid = notebookGuid
    
    # 検索結果設定：ノートタイトルのみ取得
    resultSpec = NSTypes.NotesMetadataResultSpec()
    resultSpec.includeTitle = True
    resultSpec.includeTagGuids=True

    noteCounts = noteStore.findNoteCounts(sandboxToken, filter, True)
    _index = noteCounts.notebookCounts[notebookGuid]
    index = random.randint(1,  _index )-1

    
    metalist = noteStore.findNotesMetadata(filter, index, 1, resultSpec)
    return metalist.notes[0]
        
guid=getNotebookGuidByName(choiceNotebookName)

i=0
while(i<10):
    note=randomSelectNote(guid)

    print(note.title)
    print(noteStore.getNoteContent(note.guid))
    print(note.tagGuids)

    i+=1