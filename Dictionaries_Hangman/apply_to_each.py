# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 23:35:16 2023

@author: j_edr
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]

#First

applyToEach(testList, abs)
print(testList)

#Second
def plus_one(x):
    return x+1
applyToEach(testList, plus_one)

#Third
def square(x):
    return x**2
applyToEach(testList, square)

