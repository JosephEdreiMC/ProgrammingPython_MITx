# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:43:12 2023

@author: j_edr
"""
s='azcbobobegghakl'
count=0
for n in s:
    if (n=='a' or n=='e' or n=='i' or n=='o' or n=='u'):
        count+=1

print(count)