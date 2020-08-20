import json
def jsonread():

    FileU = open('JSONTXT.json')
    reader = json.load(FileU)
    for jsons in reader:
        print(jsons)