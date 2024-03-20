def calculateBiggestSumOfThreeNumbers(a:int, b:int, c:int):
    numbersList = [a, b ,c]
    numbersList.sort()
    numbersList.pop(0)
    return numbersList[0] + numbersList[1]

def isStringPalindrom(palindrom:str):
    reversedString = palindrom[::-1]
    return palindrom.lower() == reversedString.lower()

def getLongestWordOfSentence(sentence:str):
    wordsList = sentence.split()
    longestWord = wordsList[0]

    for w in wordsList:
        if(len(longestWord) < len(w)):
            longestWord = w

    return longestWord

def doesInputContainLetterA():
    userInput:str = input()
    characters = list(userInput)
    if(userInput[0] == 'A'):
        characters[0] = 'a'

    return ''.join(characters)

def isWordAnagram(word1:str, word2:str):
    charactersWord1 = list(word1.lower())
    charactersWord2 = list(word2.lower())
    charactersWord1.sort(), charactersWord2.sort()
    return charactersWord1 == charactersWord2



if __name__ == "__main__":
    print(calculateBiggestSumOfThreeNumbers(1,2,3))
    print(isStringPalindrom("Otto"))
    print(getLongestWordOfSentence("Ich mag meinen Staubsauger sehr gerne"))
    #print(doesInputContainLetterA())
    print(isWordAnagram("Betrug", "Erbgut"))

