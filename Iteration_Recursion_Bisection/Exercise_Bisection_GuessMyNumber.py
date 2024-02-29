# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 19:49:37 2023

@author: j_edr
"""

# Guess a number between 0 and 100 using Bisection Method.
# According to the example, we need to use the integer part of the iterations
# that resulted in a 
low=0
high=100
ans=int((high+low)/2)
HighOrLow=''
print('Please think of a number between 0 and 100!')

while HighOrLow != 'c':
    print('Is your secret number ' + str(ans)+'?')
    HighOrLow=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    while (HighOrLow != 'h' and HighOrLow != 'l' and HighOrLow != 'c'):
            print('Sorry, I did not understand your input.')
            print('Is your secret number ' + str(ans)+'?')
            HighOrLow=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if HighOrLow == 'h':
        high=ans
    elif HighOrLow == 'l':
        low=ans
    ans=int((high+low)/2)

print('Game over. Your secret number was: ' + str(ans))