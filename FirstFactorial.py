# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 15:46:24 2018

@author: jmiller
"""

def FirstFactorial(num): 
    total = 1
    while num > 0:
        total = num * total
        num -= 1
    return total
    
# keep this function call here  
#print(FirstFactorial(raw_input()))
#

print(FirstFactorial(3))