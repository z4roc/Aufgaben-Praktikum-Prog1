
import json
from os import listdir
from os.path import isfile, join
import re

def saveperson(n:str, v:str, a:int, g:int):
    file = open("./FilesA5/namensliste.json", "r")

    fileContent = file.read()
    namensliste = []
    print(len(fileContent))
    if len(fileContent) > 1:
        namensliste = json.loads(fileContent)

    assert type(n) is str and type(v) is str and type(a) is int and type(g) is int

    namensliste += [{"nachname": n, "vorname": v, "alter": a, "groeße": g}]

    file.close()

    with open("FilesA5/namensliste.json", "w") as file:
        json.dump(namensliste, file)
        file.close()

def findperson(n:str):
    assert type(n) is str
    
    with open("FilesA5/namensliste.json", "r") as file:
        filecontent = file.read()

        persons = json.loads(filecontent)

        for p in persons:
            if n in p["vorname"] or n in p["nachname"]:
                print(p)
        file.close()

def removeperson(n):
    assert type(n) is str
    fileReader = open("FilesA5/namensliste.json", "r")
    fileContent = fileReader.read()

    persons = json.loads(fileContent)

    for p in persons:
            if n in p["vorname"] or n in p["nachname"]:
                persons.remove(p)

    fileReader.close()

    with open("FilesA5/namensliste.json", "w") as file:
        json.dump(persons, file)
        file.close()

def findFile(directory:str, fileName:str):
    assert type(directory) is str and type(fileName) is str
    try:
        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        for file in files:
            if re.search(fileName, file):
                print(file)

    except FileNotFoundError:
        print("Directory not found")

class MyComp12:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        return f"{self.a} + {(self.b) * 1j}"

    def __add__(self, other):
        return f"{self.a + other.a} + {(self.b + other.b) * 1j}"
    
    def __mul__(self, other):
        return f"{self.a * other.a} + {(self.b * other.b) * 1j}"
    
if __name__ == "__main__":
    print("Aufgabenblatt 5")
    #findperson("Arthur")
    #saveperson("Max", "Mustermann", 21, 180)
    #removeperson("Max")
    findFile("./FilesA5", "test")

    c1 = MyComp12(1.0, 2.0)
    c2 = MyComp12(4.0, 4.0)
    print(c1)

    print(c1 + c2)
    print(c1 * c2)



