# coding: UTF-8
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.UserStore
import evernote.edam.notestore.NoteStore
import evernote.edam.userstore.constants
import evernote.edam.notestore.ttypes as NSTypes
import evernote.edam.type.ttypes as Types
import random

evernote_token='S=s466:U=df1463c:E=1884ba979d0:C=180f3f84dd0:P=185:A=mymemo-bot:V=2:H=9387702a9000b3a5aa987b284d0c1256'
client=EvernoteClient(token=evernote_token, sandbox=False)
note_store=client.get_note_store()


def getNotebookGuidByName(notebook_name):
    notebooks=note_store.listNotebooks()

    for notebook in notebooks:
        if notebook.name == notebook_name :
            notebookGuid=notebook.guid

    return notebookGuid

def randomSelectNote(notebook_name):
    notebook_guid = getNotebookGuidByName(notebook_name)

    filter = NSTypes.NoteFilter()
    filter.notebookGuid = notebook_guid
    
    result_spec = NSTypes.NotesMetadataResultSpec()
    result_spec.includeTitle = True
    result_spec.includeTagGuids=True

    note_counts = note_store.findNoteCounts(evernote_token, filter, True)
    _index = note_counts.notebookCounts[notebook_guid]
    index = random.randint(1,  _index )-1

    meta_list = note_store.findNotesMetadata(filter, index, 1, result_spec)
    return meta_list.notes[0]

def getNoteContents(notebook_name):
    select_note = randomSelectNote(notebook_name)

    note_contents=dict()

    note_contents['title'] = ''
    if select_note.title != '無題':
        note_contents['title'] = '【' + select_note.title + '】'

    note_contents['text'] = note_store.getNoteContent(select_note.guid)

    tag_guid_list=select_note.tagGuids
    tag_list=[]

    if tag_guid_list is None :
        note_contents['tags']=None
    else:
        for tag_guid in tag_guid_list:
            tag_list.append(note_store.getTag(evernote_token, tag_guid).name)

        note_contents['tags'] = tag_list    

    return note_contents