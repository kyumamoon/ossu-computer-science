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
#print(wordlist)
#print(' '.join(wordlist))

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def giveHint(letterDict):
    wordInProgress = ""
    for i in range(len(letterDict)):
        if letterDict[i][2] == 1:
            wordInProgress = wordInProgress+letterDict[i][1]
        else:
            wordInProgress = wordInProgress+"_"
    
    #for i in wordlist:
        regexString = '^'
        for ii in range(len(wordInProgress)):
            if ii == 0:
                if letterDict[ii][2] == 0:
                    #
                    regexString = regexString+'.'
                else:
                    #regexString = regexString+letterDict[0][1]
                    regexString = regexString+wordInProgress[ii]
            else:
                if letterDict[ii][2] == 0:
                    regexString = regexString+'.'
                else:
                    #regexString = regexString+letterDict[ii][1]
                    regexString = regexString+wordInProgress[ii]

    print(regexString)
    #regexString = '^t..t'

    matches = list()
    for word in wordlist:
        if len(word) == len(wordInProgress):
            x = re.findall(regexString,word)
            if len(x) == 1:
                matches.append(x)
                #print(x)
    #print(re.findall(str(regexString),' '.join(wordlist)))
    print("")
    print("HINT:",len(matches),"POSSIBLE MATCHES:")

    if len(matches) > 0:
        for i in matches:
            print(i,end=" ")

def guessing(guess,letterDict,warnings,availableLetters,guesses):
    """
    Input: guess is a character of the guess, wordDict is a dict of the word
    Returns: bool if all letters solved.
    """
    #newWordDict = wordDict.copy()
    isFound = False
    solvedCount = 0
    isUsed = True
    isSolved = False

    if str.isalpha(guess):

            guessLower = guess.lower()

            for i in range(len(letterDict)):
                if (guessLower == letterDict[i][1]) and (letterDict[i][2] == 0):
                    letterDict[i][2] = 1
                    isFound = True
                    #print(letterDict)
            
            for i in range(len(availableLetters)):
                if availableLetters[i] == guess:
                    availableLetters[i] = "_"
                    isUsed = False
                    break

    elif guess == "*":
        giveHint(letterDict)
        return isSolved,isFound,availableLetters,guesses,warnings
                    
    newPlaceHolder = ""
    for i in range(len(letterDict)):
        if letterDict[i][2] == 1:
            newPlaceHolder = newPlaceHolder+letterDict[i][1]
            solvedCount+=1
        else:
            newPlaceHolder = newPlaceHolder+"_"

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

    if solvedCount == len(letterDict):
        isSolved = True

    return isSolved,isFound,availableLetters,guesses,warnings

    #return newWordDict

def checkAvailableLetters(string,guess):
    giveWarning = False

    if str.isalpha(guess):
        temp = guess.lower()
        for i in range(len(string)):
            if string[i] == guess:
                string[i] = "_"
                break
        print("You guessed that already! (+1 Warning)")
        giveWarning = True

        return string,giveWarning
    else:
        return string,giveWarning


def getUniqueLetters(letterDict):
    uniques = dict()
    count = 0

    for i in range(len(letterDict)):
        if letterDict[i][1] not in uniques:
            uniques[letterDict[i][1]] = 1

    for i in range(len(uniques)):
        count+=1

    return count

def hangman(x,letterDict):
    """
    Input: a string
    Functionality: plays hangman
    """
    #guessesAvailable = len(letterDict)+3
    guessesAvailable = 6
    isSolved = False
    lettersAvailable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    warnings = 0
    uniqueLetters = 0
    score = 0
    # Set up placeholders

    print("Welcome to Hangman The Game:")
    print("Your mystery word is",len(letterDict),"letters long:")
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

        checkSolved,isFound,availableLetters,guesses,warns = guessing(str.lower(guess),letterDict,warnings,lettersAvailable,guessesAvailable)

        lettersAvailable = availableLetters
        guessesAvailable = guesses
        warnings = warns

        #lettersAvailable,giveWarning = checkAvailableLetters(lettersAvailable,guess)

        if checkSolved:
            isSolved = True
            uniqueLetters = getUniqueLetters(letterDict)
            score = guessesAvailable*uniqueLetters
            break
        
        #if not isFound:
        #    guessesAvailable-=1

    if isSolved:
        print("YOU WIN WITH A SCORE OF",score,"AND",guessesAvailable,"GUESSES LEFTOVER!")
    else:
        print("YOU RAN OUT OF GUESSES.")
        print("THE WORD WAS:",x,".")

if __name__ == "__main__": 
    letterDict = list()
    #secret_word = choose_word(wordlist)
    secret_word = 'maxims'
    for i in range(len(secret_word)):
        letterDict.append([i,secret_word[i],0])
    #print(letterDict[0])
    #print(letterDict[0][0])
    #print(letterDict[0][1])
    #print(letterDict[0][2])
    print(secret_word)
    hangman(secret_word,letterDict)
    