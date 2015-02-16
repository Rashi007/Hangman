secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    k = 0
    for i in secretWord:
        if i in lettersGuessed:
            k += 1
        else:
            return False
           
    if k == len(secretWord):
        return True    
print isWordGuessed(secretWord, lettersGuessed)
