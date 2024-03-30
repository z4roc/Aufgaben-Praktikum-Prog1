# TODO: Comment the code

def calculateBiggestSumOfThreeNumbers(a:int, b:int, c:int):
    # Drei Zahlen in eine Liste umwandeln
    numbersList = [a, b ,c]
    # Liste aufsteigend sortieren und kleinstes Element mit pop-Funktion entfernen 
    numbersList.sort()
    numbersList.pop(0)
    return numbersList[0] + numbersList[1]

def isStringPalindrom(palindrom:str):
    # bei Palindrom muss der reversed String nach lower() dem Urpsurngsstring entsprechen 
    reversedString = palindrom[::-1]
    return palindrom.lower() == reversedString.lower()

def getLongestWordOfSentence(sentence:str):
    # Wörter in eine Liste an Wörtern aufteilen
    wordsList = sentence.split()
    #Initial ein längstes Wort festlegen
    longestWord = wordsList[0]

    

    for w in wordsList:
        if(len(longestWord) < len(w)):
            longestWord = w

    return longestWord

def doesInputContainLetterA():
    userInput:str = input()
    if(userInput[0] == 'A'):
        userInput = "a" + userInput[1:]
        userInput = userInput.replace("A", "a", 1)

    return userInput
    #return ''.join(characters)

def isWordAnagram(word1:str, word2:str):
    charactersWord1 = list(word1.lower())
    charactersWord2 = list(word2.lower())
    charactersWord1.sort(), charactersWord2.sort()
    return charactersWord1 == charactersWord2



if __name__ == "__main__":
    print(calculateBiggestSumOfThreeNumbers(1,2,3))
    print(isStringPalindrom("Otto"))
    print(isStringPalindrom("Hallo"))
    print(getLongestWordOfSentence("Ich muss heute eine Waschmaschine kaufen."))
    print(doesInputContainLetterA())

    print(isWordAnagram("Betrug", "Erbgut"))
    print(isWordAnagram("Hallo", "Welt"))

