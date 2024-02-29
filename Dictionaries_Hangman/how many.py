# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 09:29:43 2023

@author: j_edr
"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total_values=0
    list_keys=aDict.keys()
    for i in list_keys:
        total_values+=len(aDict[i])
    return total_values

print(how_many(aDict))
