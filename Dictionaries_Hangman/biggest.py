# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 14:26:17 2023

@author: j_edr
"""
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maximum=0
    key_maximum=''
    for i in aDict.keys():
        if len(aDict[i]) >= maximum:
            maximum=len(aDict[i])
            key_maximum=i
    return key_maximum
