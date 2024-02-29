# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:19:59 2023

@author: j_edr
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    newTuple=()
    for i in range(0,len(aTup)):
        if i%2 == 0:
            newTuple = newTuple + (aTup[i],)
    return newTuple

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))
