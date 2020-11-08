# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    total = 0
    wordGuessed = False
    for i in secretWord:
        if i in lettersGuessed:
            total += 1
            if total == len(secretWord):
                wordGuessed = True
    return wordGuessed



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = ""
    for i in list(secretWord):
        if i in lettersGuessed:
            result += i + " "
        else:
            result += '_ '
    return result



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letterPool = list('abcdefghijklmnopqrstuvwxyz')
    availableLetters = ''
    for i in letterPool:
        if i not in lettersGuessed:
            availableLetters += i
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    alpha = "abcdefghijklmnopqrstuvwxyz"
    lettersGuessed = ''
    guessesLeft = 8
    print("             ")
    print('Welcome to the game Hangman!')
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("             ")
    while not isWordGuessed(secretWord, lettersGuessed):
        if guessesLeft == 0:
            break
        else:
            print("you have " + str(guessesLeft) + " guesses left.")
            print("Available Letters: " + getAvailableLetters(lettersGuessed))
            guess = input("Please guess a letter: ")
            lowerGuess = guess.lower()
            if len(lowerGuess) != 1 or lowerGuess not in alpha:
                print("Invalid response.")
            else:
                if lowerGuess in getAvailableLetters(lettersGuessed):
                    if lowerGuess in secretWord:
                        lettersGuessed += lowerGuess
                        print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
                        print('             ')
                    elif lowerGuess not in secretWord:
                        lettersGuessed += lowerGuess
                        print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                        print('             ')
                        guessesLeft -= 1
                else:
                    print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                    print('             ')

    if guessesLeft == 0:
        print("Sorry you ran out of guesses. The word was " + str(secretWord) + ".")
    else:
        print("Congratulations, you won!")
    again = input("Would you like to play again? (y) or (n) ")
    if again == "y":
        return hangman(secretWord)
    else:
        return print("Thank you for playing!")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
