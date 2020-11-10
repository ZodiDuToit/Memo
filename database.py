import json
import os 

import random

seed = random.randint(1, 100)

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

        del data[title]

        file.truncate(0)
        file.seek(0)

        json.dump(data, file)

def retreive(title):
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data[title]


def retreiveRandomTitle():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        file.close()

    random.seed(seed)
    return random.choice(list(data.keys()))

def retreiveRandomContent():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        file.close()
  
    random.seed(seed)
    return random.choice(list(data.values()))


def retreiveAllItems():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data.items()

def retreiveAllTitles():
    with open(pathToJson, "r+") as file:
        data = json.load(file)

        return data.keys()