# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:35:57 2023

@author: j_edr
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i=min(a,b)
    while (a%i!=0 or b%i!=0):
        i-=1
    return i

print(gcdIter(168, 70))