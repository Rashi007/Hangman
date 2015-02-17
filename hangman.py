def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.
 
    Starts up an interactive game of Hangman.
 
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
 
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 0
    
    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')
 
 
    while mistakesMade < 8:
        if isWordGuessed(secretWord,lettersGuessed):
            return ('Congratulations, you won!')
        print ('You have ') + str(8-mistakesMade) + (' guesses left.')
        print ('Available letters:') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter:').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ('Oops! You\'ve already guessed that letter:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade += 1
                print ('Oops! That letter is not in my word:') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
 
 
    return ('Sorry, you ran out of guesses. The word was ') + secretWord
