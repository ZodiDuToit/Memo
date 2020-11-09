import json
import os 

jsonFileName = "memos.json"
pathToJson = os.path.join(os.path.dirname(__file__), jsonFileName)

if not os.path.isfile(pathToJson):

    with open(pathToJson, "w+") as file:
        file.write("{ }")

def insert(title, content):
    with open(pathToJson, "r+") as file:

        data = json.load(file)
        data.update({title: content})
        file.seek(0)

        json.dump(data, file)

def delete(title):
    with open(pathToJson, "r+") as file:

        data = json.load(file)
        data.discard(title)
        file.seek(0)

        json.dump(data, file)

def retreive(title):
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data[title]

def retreiveAllItems():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data.items()

def retreiveAllTitles():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data.keys()