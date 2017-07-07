def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    aStr = ''.join(sorted(aStr))
    length = len(aStr)
    mid = length // 2
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return aStr == char
    elif char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    else:
        return isIn(char, aStr[mid+1:])
