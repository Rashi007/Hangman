def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    c=0
    char=0
    for char in hand.values():
        c=c+char
    return c
