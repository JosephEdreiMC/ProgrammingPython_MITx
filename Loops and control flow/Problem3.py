# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:21:21 2023

@author: j_edr
"""
#Suppose that we are given a string 0
s='zacboboaaabegghaklaaaaaaaabbbb'
beginning_longer=0
length_longer=0
length_substring=1
i=0

while (i< len(s)-1):
    while (s[i]<=s[i+1]):
        length_substring+=1
        i+=1
        if (i == len(s)-1):
            break
    if (length_substring>length_longer):
        length_longer=length_substring
      #  print('So far, the longest string is ' + str(length_longer))
        beginning_longer=i-length_longer+1
     #   print('The start of the longer string is i=' 
     #         + str(beginning_longer))
        
    #print(length_substring)
    if(i == len(s)-1):
        break
    else:
        if(s[i]>s[i+1]):
            i+=1
        length_substring=1

print('Longest substring in alphabetical order is: '+ s[beginning_longer:
                                    beginning_longer+length_longer])
    
