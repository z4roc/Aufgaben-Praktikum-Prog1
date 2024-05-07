
import json
from os import listdir
from os.path import isfile, join
import re

def saveperson(n:str, v:str, a:int, g:int) -> None:
    file1 = open("./FilesA5/namensliste.json", "r")

    fileContent = file1.read()
    namensliste = []
    # print(len(fileContent))
    if len(fileContent) > 1:
        namensliste = json.loads(fileContent)

    assert type(n) is str and type(v) is str and type(a) is int and type(g) is int

    namensliste = [{"nachname": n, "vorname": v, "alter": a, "groeße": g}, *namensliste]

    file1.close()

    with open("FilesA5/namensliste.json", "w") as file2:
        json.dump(namensliste, file2)
        file2.close()

def findperson(n:str):
    assert type(n) is str
    person = {}
    with open("FilesA5/namensliste.json", "r") as file1:
        filecontent = file1.read()

        persons = json.loads(filecontent)

        for p in persons:
            if n in p["vorname"] or n in p["nachname"]:
                print(p)
                person = p
        file1.close()

    return person

def removeperson(n):
    assert type(n) is str
    fileReader = open("FilesA5/namensliste.json", "r")
    fileContent = fileReader.read()

    persons = json.loads(fileContent)

    for p in persons:
            if n in p["vorname"] or n in p["nachname"]:
                persons.remove(p)

    fileReader.close()

    with open("FilesA5/namensliste.json", "w") as file1:
        json.dump(persons, file1)
        file1.close()

def findFile(directory:str, fileName:str):
    assert type(directory) is str and type(fileName) is str
    try:
        files = [f for f in listdir(directory) if isfile(join(directory, f))]

        for file1 in files:
            if re.search(fileName, file1):
                print(file1)

    except FileNotFoundError:
        print("Directory not found")

class MyComp12:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
    
    def __str__(self) -> str:
        return f"{self.a} + {(self.b) * 1j}"

    def __add__(self, other):
        return MyComp12(self.a + other.a, self.b + other.b)
    
    def __mul__(self, other):
        # (a * c - bd) -> realteil * (a * d + bc)j -> imaginärteil
        return MyComp12(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)
    
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

    



