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
        for ii in range(len(letterDict)):
            if ii == 0:
                #regexString = regexString+letterDict[0][1]
                regexString = regexString+'.'
            else:
                if letterDict[ii][2] == 0:
                    regexString = regexString+'.'
                else:
                    regexString = regexString+letterDict[ii][1]

    # print(regexString)
    print("")
    print("HINT: POSSIBLE MATCHES:")
    #regexString = '^t..t'
    for word in wordlist:
        if len(word) == 4:
            x = re.findall(regexString,word)
            if len(x) == 1:
                print(x)
    #print(re.findall(str(regexString),' '.join(wordlist)))

def guessing(guess,letterDict):
    """
    Input: guess is a character of the guess, wordDict is a dict of the word
    Returns: bool if all letters solved.
    """
    #newWordDict = wordDict.copy()
    isFound = False
    solvedCount = 0

    if str.isalpha(guess):
            for i in range(len(letterDict)):
                if (guess == letterDict[i][1]) and (letterDict[i][2] == 0):
                    letterDict[i][2] = 1
                    isFound = True
                    #print(letterDict)
    elif guess == "*":
        giveHint(letterDict)
        return False,isFound
                    
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
        print("Try again!")
        print(newPlaceHolder)

    if solvedCount == len(letterDict):
        return True,isFound
    else:
        return False,isFound
    #return newWordDict

def hangman(x,letterDict):
    """
    Input: a string
    Functionality: plays hangman
    """
    guessesAvailable = len(letterDict)+3
    isSolved = False

    # Set up placeholders

    print("Playing Hangman")
    print("Your mystery word is",len(letterDict),"letters long:")

    for i in range(len(x)):
        if i==len(x)-1:
            print("_")
            print("")
        else:
            print("_",end='')
        
    print("YOU CAN USE A HINT AT ANYTIME BY ENTERING * AS A GUESS.")
    while guessesAvailable != 0:
        print("")
        print("GUESSES REMAINING:",guessesAvailable)
        guess = input("Enter you letter guess: ")
        check,found = guessing(str.lower(guess),letterDict)
        if check:
            isSolved = True
            break
        
        if not found:
            guessesAvailable-=1

    if isSolved:
        print("YOU WIN WITH",guessesAvailable,"GUESSES LEFTOVER!")
    else:
        print("YOU RAN OUT OF GUESSES.")
        print("THE WORD WAS:",x,".")

if __name__ == "__main__": 
    letterDict = list()
    #secret_word = choose_word(wordlist)
    secret_word = 'tact'
    for i in range(len(secret_word)):
        letterDict.append([i,secret_word[i],0])
    #print(letterDict[0])
    #print(letterDict[0][0])
    #print(letterDict[0][1])
    #print(letterDict[0][2])
    print(secret_word)
    hangman(secret_word,letterDict)
    