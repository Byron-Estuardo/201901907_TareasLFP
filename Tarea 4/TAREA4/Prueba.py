def jsonread():
    import json
    FileU = open('Practica1.json')
    reader = json.load(FileU)
    FileU.close()
    lista = list()
    for jsons in reader:
        lista.append(jsons)
    return reader