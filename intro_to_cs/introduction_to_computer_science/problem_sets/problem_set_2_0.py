import random
import re

WORDLIST_FILENAME = "problem_set_2_words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

wordlist = load_words()

def choose_word(wordlist):
    """
    Input: wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def giveHint(chosenWordValues):
    """
    Input: list of checking values of chosen word
    Functionality: find all matching words from word list that has same length and guesses characters of same index positions. Uses regex.
    """

    wordInProgress = ""
    for i in range(len(chosenWordValues)):
        if chosenWordValues[i][2] == 1:
            wordInProgress = wordInProgress+chosenWordValues[i][1]
        else:
            wordInProgress = wordInProgress+"_"
    

    regexString = '^'
    for i in range(len(wordInProgress)):
        if i == 0:
            if chosenWordValues[i][2] == 0:
                regexString = regexString+'.'
            else:
                 regexString = regexString+wordInProgress[i]
        else:
            if chosenWordValues[i][2] == 0:
                regexString = regexString+'.'
            else:
                regexString = regexString+wordInProgress[i]

    matches = list()
    for word in wordlist:
        if len(word) == len(wordInProgress):
            x = re.findall(regexString,word)
            if len(x) == 1:
                matches.append(x)

    print("")
    print("HINT:",len(matches),"POSSIBLE MATCHES:")

    if len(matches) > 0:
        for i in matches:
            print(i,end=" ")
        print('')

def printPlaceholder(chosenWordValues,solvedCount):
    """
    Input: choseWordValues is a list of checking values for chosen word
    Input: solved count is int
    Returns: a string and int
    Functionality: function goes through list and see which characters are guessed or not and count guessed, it also creates a placeholder for unguessed characters in the word.

    """
    placeholder = ""

    for i in range(len(chosenWordValues)):
        if chosenWordValues[i][2] == 1:
            placeholder = placeholder+chosenWordValues[i][1]
            solvedCount+=1
        else:
            placeholder = placeholder+"_"
    
    return placeholder,solvedCount

def guessing(guess,chosenWordValues,warnings,availableLetters,guesses):
    """
    Input: guess is a character of the guess
    Input: chosenWordValues is a list with checking values
    Input: warnings is an int
    Input: availableLetters is a list
    Input: guesses is a int
    Returns: bool, list, int, int
    Functionality: main game logic
    """
    isFound = False
    isUsed = True
    isSolved = False
    solvedCount = 0

    if str.isalpha(guess):

            guessLower = guess.lower()

            for i in range(len(chosenWordValues)):
                if (guessLower == chosenWordValues[i][1]) and (chosenWordValues[i][2] == 0):
                    chosenWordValues[i][2] = 1
                    isFound = True
            
            for i in range(len(availableLetters)):
                if availableLetters[i] == guess:
                    availableLetters[i] = "_"
                    isUsed = False
                    break

    elif guess == "*":
        giveHint(chosenWordValues)
        return isSolved,availableLetters,guesses,warnings
                    
    newPlaceHolder,count = printPlaceholder(chosenWordValues,solvedCount)
    solvedCount = count

    if isFound:
        print("Nice! Your guess was in the word!")
        print(newPlaceHolder)
    else:
        if isUsed == True and str.isalpha(guess):
            print("You already used this letter!")
            if warnings < 3:
                warnings+=1
                print("You have",warnings,"out of 3 before you lose a guess.")
            else:
                print("You lost a guess for using the same character...")
                guesses-=1
        elif isUsed == True and not str.isalpha(guess):
            print("You can't use numbers or special characters!")   
            if warnings < 3:
                warnings+=1
                print("You have",warnings,"out of 3 before you lose a guess.")
            else:
                print("You lost a guess for using a number/special character...")
                guesses-=1
        else:
            if guess in ['a','e','i','o','u']:
                guesses-=2
            else:
                guesses-=1

        print("Try again!")
        print("WORD:",newPlaceHolder)

    if solvedCount == len(chosenWordValues):
        isSolved = True

    return isSolved,availableLetters,guesses,warnings

def getUniqueLetters(chosenWordValues):
    """
    Input: chosenWordValues, a dictionary with each character of chosen word as the values
    Return: count of unique characters in the word.
    """

    uniques = dict()
    count = 0

    for i in range(len(chosenWordValues)):
        if chosenWordValues[i][1] not in uniques:
            uniques[chosenWordValues[i][1]] = 1
            count+=1

    return count

def hangman(x,chosenWordValues):
    """
    Input: x, a string which is the randomly chosen word
    Input: chosenWordValues, a list to track each letter of the word that is chosen
    Functionality: plays hangman
    """

    lettersAvailable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    isSolved = False
    guessesAvailable = 6
    warnings = 0
    uniqueLetters = 0
    score = 0

    print("Welcome to Hangman The Game:")
    print("Your mystery word is",len(chosenWordValues),"letters long:")
    print("WORD:",end="")

    for i in range(len(x)):
        if i==len(x)-1:
            print("_")
            print("")
        else:
            print("_",end='')
        
    print("YOU CAN USE A HINT AT ANYTIME BY ENTERING * AS A GUESS.")

    while guessesAvailable != 0:
        print("//---------------------------------//")
        print("Guesses Remaining:",guessesAvailable)

        unusedL = ''.join(lettersAvailable)
        print("Unused letters:",unusedL)

        guess = input("Enter a letter guess: ")
        checkSolved,availableLetters,guesses,warns = guessing(str.lower(guess),chosenWordValues,warnings,lettersAvailable,guessesAvailable)

        lettersAvailable = availableLetters
        guessesAvailable = guesses
        warnings = warns

        if checkSolved:
            isSolved = True
            uniqueLetters = getUniqueLetters(chosenWordValues)
            score = guessesAvailable*uniqueLetters
            break

    if isSolved:
        print("YOU WIN WITH A SCORE OF",score,"AND",guessesAvailable,"GUESSES LEFTOVER!")
    else:
        print("YOU RAN OUT OF GUESSES.")
        print("THE WORD WAS:",x,".")

if __name__ == "__main__":
    """
    Setup the startup variables.
    Bot picks random word from list.
    """
    chosenWordList = list()
    secret_word = choose_word(wordlist)
    for i in range(len(secret_word)):
        chosenWordList.append([i,secret_word[i],0])
    hangman(secret_word,chosenWordList)
    
    