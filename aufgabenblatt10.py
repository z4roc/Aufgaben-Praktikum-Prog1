import functools
import os

# Relative Filepath
os.chdir("./FilesA10")
# Absolute wäre C:\Users\arthu\repos\z4roc\aufgaben\FilesA10

def cleanupList(liste):
    return functools.reduce(lambda x, y: x + y, liste)

def maxListSize(liste):
    return functools.reduce(lambda x, y: max(str(x), str(y)), liste)

def getLineLength(filename) -> list:
    return [len(l) for l in open(filename, "r")]

def getFirstThreeRows(filename) -> list:
    return [l for l in open(filename, "r")][:3]

def revereseFirstLine(filename) -> str:
    return [l[::-1] for l in open(filename, "r")][0]

def lengthOfFirstWord(filename) -> list:
    return [len(l.split(" ")[0]) for l in open(filename, "r")]

def lineNumberOfLinesWithNoSpaces(filename) -> list:
    return [l for l, m in enumerate(open(filename, "r"), 1) if any(letter == " " for letter in m)]

def allFilesWithEnding() -> list:
    return[f for f in os.listdir() if ".py" in f]

def allFilesWithLength() -> list:
     # print([len(open(f, "r").read()) for f in os.listdir()])
    return[f for f in os.listdir() if len(f) > 10 and len(open(f, "r").read()) > 10]

if __name__ == "__main__":
    lst = [(1, 10), ('a', 'b'), ([1], [2])]
    print(cleanupList(lst))
    print(maxListSize(lst))
    print(getLineLength("test.txt"))
    print(getFirstThreeRows("test.txt"))
    print(revereseFirstLine("test.txt"))
    print(lengthOfFirstWord("test.txt"))
    print(lineNumberOfLinesWithNoSpaces("test.txt"))
    print(allFilesWithEnding())
    print(allFilesWithLength())

