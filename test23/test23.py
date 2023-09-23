

import datetime
import json
import os

sourceForNotes = "test23/notes"
selectTypeFile = "*_note_*.json"

sourceForSettings = "test23/settings"
selectFileSettings = "settings.json"

def readJSON (source, selctedNameFile):
    os.chdir(source)
    with open (selctedNameFile) as f:
            stringJSON = json.loads(f)
    return stringJSON

def writeInFile (source, selctedNameFile, objForWrite):
    os.chdir(source)
    with open (selctedNameFile, 'w') as f:
        json.dump(objForWrite, f)




print("Введите заголовок для заметки:")
headnote = str(input())
if (len(headnote) == 0):
    headnote = "Unname"
print("Введите основной текст заметки:")
bodynote = str(input())
if (len(bodynote) == 0):
    bodynote = "Enter text for note, please"

settingMaxID = readJSON(sourceForSettings, selectFileSettings)

newNote = {"idNote" : settingMaxID['maxID'] + 1, "lastdate" : str(datetime.datetime.now()), "headnote": headnote, "bodynote" : bodynote }
settingMaxID['maxID'] = newNote['idNote']
newFileName = str(newNote['idNote']) + "_note_" + str(newNote['headnote']) + ".json"

writeInFile(sourceForSettings, selectFileSettings, settingMaxID)
writeInFile(sourceForNotes, newFileName, newNote)
