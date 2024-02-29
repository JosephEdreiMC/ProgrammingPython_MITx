# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 00:05:26 2023

@author: j_edr
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Determine the mid-index of aStr
    if aStr=='':
        return False
    middle=len(aStr)//2
    # One base case occurs when the middle of the string is equal to char
    if char==aStr[middle]:
        return True
    # It is suggested to specifically consider the case when aStr consists
    # of one character
    elif len(aStr)==1:
        return aStr==char
    else:
    # Now, we need to consider the cases when the character is not in the 
    # upper half or lower half.
        if (aStr[middle] > char):
            return isIn(char, aStr[0:middle])
        else:
            return isIn(char, aStr[middle+1:])
print(isIn('x', 'aaefhiijkkllmmnsswyz'))