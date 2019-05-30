# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:42:51 2018

@author: jmiller
"""

def LetterChanges(str): 
    import string
    new_str = ''
    for letter in str:
        if letter in string.ascii_letters:
            new_letter = string.ascii_letters[string.ascii_letters.\
                                              index(letter) + 1]
        else:
            new_letter = letter
        if new_letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            new_letter = new_letter.upper()
        new_str += new_letter
    return new_str
    
# keep this function call here  
#print LetterChanges(raw_input())  