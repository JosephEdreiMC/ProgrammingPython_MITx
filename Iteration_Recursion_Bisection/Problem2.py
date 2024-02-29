# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 19:09:00 2023

@author: j_edr
"""

balance = 3926
annualInterestRate = 0.2
balance_end=balance
monthly=10
while balance_end > 0:
    balance_end=balance
    for i in range(1,13):
        balance_end = balance_end - monthly
        balance_end = balance_end + (annualInterestRate/12.0)*balance_end
    monthly+=10
print(monthly-10)