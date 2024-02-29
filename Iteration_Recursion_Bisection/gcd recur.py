# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 14:47:59 2023

@author: j_edr
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
# Notice that it does not include an ELSE
    return gcdRecur(b, a % b)     
    
    