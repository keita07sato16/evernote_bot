# coding: UTF-8
from evernote.api.client import EvernoteClient
import evernote.edam.userstore.UserStore
import evernote.edam.notestore.NoteStore
import evernote.edam.userstore.constants
import evernote.edam.notestore.ttypes as NSTypes
import evernote.edam.type.ttypes as Types
import random

sandboxToken='S=s466:U=df1463c:E=1884ba979d0:C=180f3f84dd0:P=185:A=mymemo-bot:V=2:H=9387702a9000b3a5aa987b284d0c1256'
client=EvernoteClient(token=sandboxToken, sandbox=False)
noteStore=client.get_note_store()


def getNotebookGuidByName(notebook_name):
    notebooks=noteStore.listNotebooks()

    for notebook in notebooks:
        if notebook.name == notebook_name :
            notebookGuid=notebook.guid

    return notebookGuid

def randomSelectNote(notebook_name):
    notebook_guid = getNotebookGuidByName(notebook_name)

    filter = NSTypes.NoteFilter()
    filter.notebookGuid = notebook_guid
    
    resultSpec = NSTypes.NotesMetadataResultSpec()
    resultSpec.includeTitle = True
    resultSpec.includeTagGuids=True

    noteCounts = noteStore.findNoteCounts(sandboxToken, filter, True)
    _index = noteCounts.notebookCounts[notebook_guid]
    index = random.randint(1,  _index )-1

    metalist = noteStore.findNotesMetadata(filter, index, 1, resultSpec)
    return metalist.notes[0]

def getNoteContents(notebook_name):
    select_note = randomSelectNote(notebook_name)

    note_contents=dict()

    note_contents["title"]=""
    if select_note.title != "無題":
        note_contents["title"]="【"+select_note.title+"】"

    note_contents["text"]=noteStore.getNoteContent(select_note.guid)

    tag_guid_list=select_note.tagGuids
    tag_list=[]

    if tag_guid_list is None :
        note_contents["tags"]=None
    else:
        for tag_guid in tag_guid_list:
            tag_list.append(noteStore.getTag(sandboxToken, tag_guid).name)

        note_contents["tags"]=tag_list    

    return note_contents