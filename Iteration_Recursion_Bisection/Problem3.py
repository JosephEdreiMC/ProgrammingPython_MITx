# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:33:19 2023

@author: j_edr
"""
balance = 999999
annualInterestRate = 0.18

initialLower = balance/12
initialUpper = (balance*(1+annualInterestRate/12)**12)/12
midpoint1 = (initialLower + initialUpper)/2

'''
The bisection is over a continuum of real numbers; therefore, we need
set an epsilon so that we stop the recursion
'''
# Find the final balance given a FIXED monthly payment

def final_balance(balance, annualInterestRate, payment):
    for i in range(1,13):
        balance = balance - payment
        balance = balance + (annualInterestRate/12.0)*balance
    return balance

# Recursive bisection function

def bisect(balance, annualInterestRate, epsilon, payment, lower, upper):
    currentBalance=final_balance(balance, annualInterestRate, payment)
    # Base case, balance small enough
    if abs(currentBalance) <= epsilon:
        return round(payment, 2)
    # Recursion when midpoint is too high
    if currentBalance < -epsilon:
        return bisect(balance, annualInterestRate, epsilon, (payment+lower)/2, 
                      lower, payment)
    # Recursion when midpoint is too low
    if currentBalance > epsilon:
        return bisect(balance, annualInterestRate, epsilon, (payment+upper)/2, 
                      payment, upper)

result=bisect(balance, annualInterestRate, 0.01, midpoint1, initialLower, initialUpper)

print('Lowest Payment: ' + str(result))
