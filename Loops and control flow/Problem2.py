# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:50:43 2023

@author: j_edr
"""

s = 'xhtbobboboboobobboboboobobbbobbyahbobbbob'
s_3=''
count_bob=0
for i in range(len(s)):
    s_3=s[i:i+3]
    if (s_3=='bob'):
        count_bob+=1
print(count_bob)

# What's the code doing when i=len(s)?
#print(s_3)