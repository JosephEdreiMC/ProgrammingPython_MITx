# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:02:32 2023

@author: j_edr
"""

def genPrimes():
    primes=[2]
    yield primes[-1]
    x=2
    while True:
        x += 1
        counter=0
        for p in primes:
            if (x % p) !=0:
                counter += 0
            else:
                counter +=1
        if counter == 0:
            primes.append(x)
            yield primes[-1]
            
# Official solution makes use of a FOR/ELSE clause
'''
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
'''                