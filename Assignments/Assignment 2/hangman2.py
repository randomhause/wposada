# Hangman game
#Status: error in line 184

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

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

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if secretWord=='':
      return True
    for c in secretWord:
      if c in lettersGuessed:
        return isWordGuessed(secretWord[1:], lettersGuessed)
      elif c not in lettersGuessed:
        return False
#When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = 0 
    empty = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord): #Index Lists for letters guessed
      if c in lettersGuessed:
        count += 1
        empty.insert(count-1, c) #inserts object before index
        empty.pop(count) #takes out letters guessed
        if count == len(secretWord):
          return ''.join(str(e) for e in empty)
      else:
        count += 1 
        empty.insert(count-1, '_')
        empty.pop(count)
        if count == len(secretWord):
          return ''.join(str(e) for e in empty)


# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet2 = alphabet[:]

    def remove_duplicate(L1, L2):
      L1beg = L1[:]
      for e in L1: 
        if e in L1beg:
          L2.remove(e)
      return ''.join(str(e) for e in L2)
    return remove_duplicate(lettersGuessed, alphabet2)



# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


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

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", str(len(secretWord)), "letters long.")
    print("-------------")
    
    guessLeft=8
    lettersGuessed=[]
    guess = input('Please guess a letter: ').lower()
    #guess=guess.lower()
    
    while guessLeft > 0 and not isWordGuessed(secretWord, lettersGuessed):
      print('You have', str(guessLeft), 'guesses left!')
      print('Available letters:', getAvailableLetters)
    
    while len(guess)!= 1 and guess not in  string.ascii_lowercase:
      guess=str(raw_input('Please guess a new letter: '))
    if guess not in lettersGuessed:
      print('Correct: ')
      else: guessLeft -=1
        print('That letter is not in my word'),
      else:
        print('You have already guessed that letter: '),
      print(getGuessedWord(secretWord, lettersGuessed))
      print('-------------')
    if isWordGuessed(secretWord, lettersGuessed)
      print('-------------')
    else:
      print('You have ran out of guesses. The word was', str(secretWord))
             
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
