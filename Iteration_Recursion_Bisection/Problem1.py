# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 18:33:06 2023

@author: j_edr
"""

balance=42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(1,13):
    balance = balance - balance*monthlyPaymentRate
    balance = round(balance + (annualInterestRate/12.0)*balance, 2)
    #print ('Month', i, 'Remaining balance: ', balance)

print('Remaining balance: ', round(balance, 2))    
    