import os.path
import json


class crearjson:

    def __init__(self, filename):
        self.filename = filename if filename == None else 'jsonSensores.json'

    def getDataJson(self):
        data = []
        if (os.path.isfile(self.filename)):
            file = open(self.filename, "r")
            data = json.loads(file.read())
        return data

    def toJson(self, listaProducto):
        file = open(self.filename, "w")
        file = json.dump([ob.__dict__ for ob in listaProducto], file, indent=4)