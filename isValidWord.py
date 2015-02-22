def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    u=hand.copy()
    if word not in wordList:
        return False
    else:
        for char in word:
         
            if char not in u.keys() or u[char]==0:
                return False
            if char in u.keys():
                u[char]=u[char]-1
        return True
